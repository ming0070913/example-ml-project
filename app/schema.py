#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class InferenceInput(BaseModel):
    """
    Input values for model inference
    """
    sepal_length: float = Field(..., example=3.1, gt=0, title='sepal length (cm)')
    sepal_width: float = Field(..., example=3.5, gt=0, title='sepal width (cm)')
    petal_length: float = Field(..., example=3.4, gt=0, title='petal length (cm)')
    petal_width: float = Field(..., example=3.0, gt=0, title='petal width (cm)')


class InferenceResult(BaseModel):
    """
    Inference result from the model
    """
    setosa: float = Field(..., example=0.987526, title='Probablity for class setosa')
    versicolor: float = Field(..., example=0.000015, title='Probablity for class versicolor')
    virginica: float = Field(..., example=0.012459, title='Probablity for class virginica')
    pred: str = Field(..., example='versicolor', title='Predicted class with highest probablity')


class InferenceResponse(BaseModel):
    """
    Output response for model inference
    """
    error: bool = Field(..., example=False, title='Whether there is error')
    results: InferenceResult = ...


class ErrorResponse(BaseModel):
    """
    Error response for the API
    """
    error: bool = Field(..., example=True, title='Whether there is error')
    message: str = Field(..., example='', title='Error message')
    traceback: str = Field(None, example='', title='Detailed traceback of the error')
