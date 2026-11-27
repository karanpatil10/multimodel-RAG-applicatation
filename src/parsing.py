import json 
#Reads and writes JSON data 
#(like chunk metadata, manifests, or saved results)

import sys 
#Accesses Python runtime settings 
# and module search paths (sys.path).

from pathlib import path 
#Handles file and folder paths 
# cleanly across operating systems

from typing import list, Any, dict, Option
#Adds type hints for flexible values

PROJECT_ROOT = path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0,str(PROJECT_ROOT))
#Finds your project root folder 
# and adds it to Python's import search 
# list so module imports work 
# regardless of where you run the script.

import pymupdf as fitz
#High-speed PDF parsing, text extraction,
#  page rendering, and image extraction

import pandas as pd
#Tabular data manipulation and structuring

import pdfplumber
#Fine-grained PDF layout and table extraction

import pytesseract
#Python wrapper for the Tesseract 
# OCR(optical character recognitation) 
# for images charts screenshots embedded images

from PIL import Images
#Image loading, cropping, resizing, 
# and format conversion via Pillow

from Langchain_core.documents import Document
#Standard document container 
# (page_content + metadata) 
# used across LangChain workflows.

from exceptation.custom_exception import DocumentPortalException
#Project-specific custom exception class for consistent error reporting.

from logger.custom_logger import CustomLogger
#Project-specific logging utility for tracking pipeline execution

logger = CustomLogger().get_logger(__name__)
#logger setup

class ComplexPDFParser:
    def __init__(
            self,
            pdf_path: str,
            output_dir: str,
            tesseract_path: optional[str]= None,
            render_scale: float = 2.0,
    ):
        self.pdf_path = path(pdf_path)
        self.output_dir = path(output_dir)
        self.image_dir = self.output_dir/"extracted_images"
        self.page_image_dir = self.output_dir/ "page_images"
        self.render_scale = render_scale

        try:
            self._validate_pdf()
            self._create_output_directories()
            self._configure_tesseract(tesseract_path)
            logger.info(
                "pdf_parser_initialized"
                pdf_path=str(self.pdf_path),
                output_dir=str(self.output_dir),
            )
        except Exceptation as exc:
            logger.exceptation(
                "pdf_parser_initalizatation_failed"
                pdf_path=str(self.pdf_path)
                error=str(exc),
            )
            raise DocumentPortalExceptation(
                "Failed to initalized the pdf parser"
                exc,
            )from exc
