# -----------------------------
# HIPE-2026 JSONL Validation Makefile
# -----------------------------

VERSION = v1.0
SCHEMA = schemas/data_schema-$(VERSION).json
VALIDATOR = scripts/check_jsonlschema.py
DATA_DIR = data/$(VERSION)
JSONL_FILES = $(wildcard $(DATA_DIR)/*.jsonl)
PYTHON = python3

.PHONY: help validate validate-all install clean

help:
	@echo ""
	@echo "HIPE-2026 Data Validation"
	@echo "-------------------------"
	@echo "VERSION: $(VERSION)"
	@echo ""
	@echo "make validate          - Validate JSONL files in data/$(VERSION)/"
	@echo "make install           - Install required Python packages"
	@echo "make clean             - Remove temporary files and virual environments"
	@echo ""

venv: requirements.txt
	$(PYTHON) -m venv venv && . venv/bin/activate && pip install -r requirements.txt

install: venv

validate: | venv
	. venv/bin/activate && $(PYTHON) $(VALIDATOR) --schemafile $(SCHEMA) $(JSONL_FILES)

clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	rm -rvf venv
