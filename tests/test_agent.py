import json

import pytest

from buscalar.config import REQUIRED_CITIES, WEIGHTS
from buscalar.models import Observation, ValidationError
from buscalar.ranking import weighted_score
from buscalar.report import render_report
from buscalar.storage import AppendOnlyStore
from buscalar.prompts import research_plan


def observation(**overrides):
    value = {
        "kind": "venda",
        "city": "Tatuí",
        "collected_at": "2026-08-13T12:00:00-03:00",
        "source": "Portal",
        "url": "https://example.com/imovel/123",
        "confidence": "Média confiança",
        "evidence_type": "fato",
        "data": {"bairro": "Centro", "tipo": "casa", "quartos": 3, "preco": 480000, "area_construida": 120},
    }
    value.update(overrides)
    return Observation.from_dict(value)


def test_all_required_cities_and_weights_are_preserved():
    assert len(REQUIRED_CITIES) == 15
    assert sum(WEIGHTS.values()) == pytest.approx(1)
    assert "Santa Bárbara d'Oeste" in REQUIRED_CITIES


def test_rejects_out_of_budget_or_non_house_sale():
    with pytest.raises(ValidationError, match="excede"):
        observation(data={"bairro": "Centro", "tipo": "casa", "quartos": 3, "preco": 500001})
    with pytest.raises(ValidationError, match="apenas casa"):
        observation(data={"bairro": "Centro", "tipo": "apartamento", "quartos": 3, "preco": 450000})


def test_store_is_append_only_and_deduplicates(tmp_path):
    store = AppendOnlyStore(tmp_path)
    item = observation()
    assert store.ingest([item]) == (1, 0)
    assert store.ingest([item]) == (0, 1)
    rows = json.loads((tmp_path / "data" / "imoveis-venda.json").read_text())
    assert len(rows) == 1


def test_partial_score_exposes_coverage_instead_of_assuming_zero():
    score = weighted_score({"seguranca": 8, "qualidade_ar": 6})
    assert score.final == pytest.approx(7.14)
    assert score.coverage == 35.0
    assert "aluguel" in score.missing


def test_empty_report_contains_every_city_and_no_fabricated_ranking():
    report = render_report([])
    assert report.startswith("# Relatório BuscaLar")
    assert all(city in report for city in REQUIRED_CITIES)
    assert "Não confirmado" in report
    assert "Parte 14 — Recomendação final" in report


def test_research_plan_uses_buscalar_brand():
    assert research_plan().startswith("# Plano de execução — BuscaLar")
