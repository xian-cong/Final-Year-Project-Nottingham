/**
  ******************************************************************************
  * @file    emotion_model_data_params.h
  * @author  AST Embedded Analytics Research Platform
  * @date    Thu Feb  8 15:59:54 2024
  * @brief   AI Tool Automatic Code Generator for Embedded NN computing
  ******************************************************************************
  * Copyright (c) 2024 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  ******************************************************************************
  */

#ifndef EMOTION_MODEL_DATA_PARAMS_H
#define EMOTION_MODEL_DATA_PARAMS_H
#pragma once

#include "ai_platform.h"

/*
#define AI_EMOTION_MODEL_DATA_WEIGHTS_PARAMS \
  (AI_HANDLE_PTR(&ai_emotion_model_data_weights_params[1]))
*/

#define AI_EMOTION_MODEL_DATA_CONFIG               (NULL)


#define AI_EMOTION_MODEL_DATA_ACTIVATIONS_SIZES \
  { 2128, }
#define AI_EMOTION_MODEL_DATA_ACTIVATIONS_SIZE     (2128)
#define AI_EMOTION_MODEL_DATA_ACTIVATIONS_COUNT    (1)
#define AI_EMOTION_MODEL_DATA_ACTIVATION_1_SIZE    (2128)



#define AI_EMOTION_MODEL_DATA_WEIGHTS_SIZES \
  { 9176, }
#define AI_EMOTION_MODEL_DATA_WEIGHTS_SIZE         (9176)
#define AI_EMOTION_MODEL_DATA_WEIGHTS_COUNT        (1)
#define AI_EMOTION_MODEL_DATA_WEIGHT_1_SIZE        (9176)



#define AI_EMOTION_MODEL_DATA_ACTIVATIONS_TABLE_GET() \
  (&g_emotion_model_activations_table[1])

extern ai_handle g_emotion_model_activations_table[1 + 2];



#define AI_EMOTION_MODEL_DATA_WEIGHTS_TABLE_GET() \
  (&g_emotion_model_weights_table[1])

extern ai_handle g_emotion_model_weights_table[1 + 2];


#endif    /* EMOTION_MODEL_DATA_PARAMS_H */
