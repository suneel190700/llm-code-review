"""
LLM-Powered Code Review Assistant
Author: Suneel Kalva
"""

import os
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
