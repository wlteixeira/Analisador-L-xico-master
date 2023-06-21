
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRE_CHAV ABRE_COLCH ABRE_PAR BOOLEANO BOOLEANOREAL CADEIA_CAR CADEIA_CAR COMPILADORES ENQUANTO ENQUANTO ESCREVA ESCREVA FECHA_CHAV FECHA_COLCH FECHA_PAR FIM FUNK FUNK IFSULDEMINAS INICIO INT INTEIRO ITERADORES LEIA LEIA NEGACAO NOME_FUNK NUM_ERRO OPER_ATRIB_IGUAL OPER_LOG OPER_MAT OPER_RELA PARA PARA PONTO_VIRG REAL RETORNA RETORNO SE SE SENAO SENAO STR_INCOMPLETA TIPO VAR VAR_ERRO VIRGcodigo : IFSULDEMINAScodigo : COMPILADOREScodigo : INICIOcodigo : FIMcodigos : codigos codigocodigos : codigocodigo : TIPO VAR \n                | TIPO VAR OPER_ATRIB_IGUAL INTEIRO\n                | TIPO VAR OPER_ATRIB_IGUAL REAL\n                | TIPO VAR OPER_ATRIB_IGUAL CADEIA_CAR\n                | TIPO VAR OPER_ATRIB_IGUAL BOOLEANO \n                | TIPO VAR OPER_ATRIB_IGUAL VAR\n    codigo : INT\n            | REAL\n            | BOOLEANO\n            | CADEIA_CAR\n    codigo : PARA ABRE_PAR VAR OPER_ATRIB_IGUAL VAR PONTO_VIRG VAR OPER_RELA VAR PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n            | PARA ABRE_PAR VAR OPER_RELA VAR PONTO_VIRG VAR OPER_RELA VAR PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n            | PARA ABRE_PAR VAR OPER_ATRIB_IGUAL VAR PONTO_VIRG VAR OPER_RELA INTEIRO PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n            | PARA ABRE_PAR VAR OPER_RELA VAR PONTO_VIRG VAR OPER_RELA INTEIRO PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n\n            | PARA ABRE_PAR VAR OPER_ATRIB_IGUAL INTEIRO PONTO_VIRG VAR OPER_RELA INTEIRO PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n            | PARA ABRE_PAR VAR OPER_RELA INTEIRO PONTO_VIRG VAR OPER_RELA VAR PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n    codigo : SE ABRE_PAR VAR OPER_RELA VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n                   | SE ABRE_PAR VAR OPER_RELA INTEIRO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n                   | SE ABRE_PAR VAR OPER_RELA CADEIA_CAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n                   | SE ABRE_PAR VAR OPER_RELA BOOLEANO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n                   | SE ABRE_PAR VAR OPER_RELA REAL FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n\n                   | SE ABRE_PAR VAR OPER_RELA VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV SENAO ABRE_CHAV codigos FECHA_CHAV\n                   | SE ABRE_PAR VAR OPER_RELA INTEIRO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV SENAO ABRE_CHAV codigos FECHA_CHAV\n                   | SE ABRE_PAR VAR OPER_RELA CADEIA_CAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV SENAO ABRE_CHAV codigos FECHA_CHAV\n                   | SE ABRE_PAR VAR OPER_RELA BOOLEANO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV SENAO ABRE_CHAV codigos FECHA_CHAV\n                   | SE ABRE_PAR VAR OPER_RELA REAL FECHA_PAR ABRE_CHAV codigos FECHA_CHAV SENAO ABRE_CHAV codigos FECHA_CHAV\n        codigo : ENQUANTO ABRE_PAR VAR OPER_RELA VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n              | ENQUANTO ABRE_PAR VAR OPER_RELA INTEIRO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n              | ENQUANTO ABRE_PAR VAR OPER_RELA REAL FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n              | ENQUANTO ABRE_PAR VAR OPER_RELA BOOLEANO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n              | ENQUANTO ABRE_PAR VAR OPER_RELA CADEIA_CAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n    codigo : RETORNO ABRE_PAR VAR FECHA_PAR\n              | RETORNO INTEIRO\n    codigo : FUNK NOME_FUNK ABRE_PAR VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n              | FUNK NOME_FUNK ABRE_PAR VAR VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n              | FUNK NOME_FUNK ABRE_PAR VAR VAR VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n              | FUNK NOME_FUNK ABRE_PAR VAR VAR VAR VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n              | FUNK NOME_FUNK ABRE_PAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV\n    codigo : NOME_FUNK ABRE_PAR VAR FECHA_PAR\n              | NOME_FUNK ABRE_PAR VAR VAR FECHA_PAR\n              | NOME_FUNK ABRE_PAR VAR VAR VAR FECHA_PAR\n              | NOME_FUNK ABRE_PAR VAR VAR VAR VAR FECHA_PAR\n              | NOME_FUNK ABRE_PAR FECHA_PAR\n    codigo : ESCREVA ABRE_PAR CADEIA_CAR FECHA_PAR\n            | ESCREVA ABRE_PAR CADEIA_CAR VAR FECHA_PAR\n            | ESCREVA ABRE_PAR VAR FECHA_PAR\n            | ESCREVA ABRE_PAR CADEIA_CAR INTEIRO FECHA_PAR\n            | ESCREVA ABRE_PAR INTEIRO FECHA_PAR\n            | ESCREVA ABRE_PAR CADEIA_CAR REAL FECHA_PAR\n            | ESCREVA ABRE_PAR REAL FECHA_PAR\n\n  codigo : LEIA ABRE_PAR VAR FECHA_PAR'
    
_lr_action_items = {'IFSULDEMINAS':([0,2,3,4,5,7,8,9,10,19,24,36,42,43,44,45,46,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[2,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,-49,-12,-8,-9,-10,-11,-38,-45,-50,-52,-54,-56,-57,2,-46,-51,-53,-55,2,2,-6,-47,2,2,2,2,2,2,2,2,2,2,2,2,-44,-5,-48,2,2,2,2,2,2,2,2,2,2,2,2,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,2,2,-41,2,-42,2,2,2,2,2,-43,2,2,2,2,2,-28,-29,-30,-31,-32,2,2,2,2,2,2,2,2,2,2,2,2,-17,-19,-21,-18,-20,-22,]),'COMPILADORES':([0,2,3,4,5,7,8,9,10,19,24,36,42,43,44,45,46,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[3,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,-49,-12,-8,-9,-10,-11,-38,-45,-50,-52,-54,-56,-57,3,-46,-51,-53,-55,3,3,-6,-47,3,3,3,3,3,3,3,3,3,3,3,3,-44,-5,-48,3,3,3,3,3,3,3,3,3,3,3,3,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,3,3,-41,3,-42,3,3,3,3,3,-43,3,3,3,3,3,-28,-29,-30,-31,-32,3,3,3,3,3,3,3,3,3,3,3,3,-17,-19,-21,-18,-20,-22,]),'INICIO':([0,2,3,4,5,7,8,9,10,19,24,36,42,43,44,45,46,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[4,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,-49,-12,-8,-9,-10,-11,-38,-45,-50,-52,-54,-56,-57,4,-46,-51,-53,-55,4,4,-6,-47,4,4,4,4,4,4,4,4,4,4,4,4,-44,-5,-48,4,4,4,4,4,4,4,4,4,4,4,4,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,4,4,-41,4,-42,4,4,4,4,4,-43,4,4,4,4,4,-28,-29,-30,-31,-32,4,4,4,4,4,4,4,4,4,4,4,4,-17,-19,-21,-18,-20,-22,]),'FIM':([0,2,3,4,5,7,8,9,10,19,24,36,42,43,44,45,46,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[5,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,-49,-12,-8,-9,-10,-11,-38,-45,-50,-52,-54,-56,-57,5,-46,-51,-53,-55,5,5,-6,-47,5,5,5,5,5,5,5,5,5,5,5,5,-44,-5,-48,5,5,5,5,5,5,5,5,5,5,5,5,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,5,5,-41,5,-42,5,5,5,5,5,-43,5,5,5,5,5,-28,-29,-30,-31,-32,5,5,5,5,5,5,5,5,5,5,5,5,-17,-19,-21,-18,-20,-22,]),'TIPO':([0,2,3,4,5,7,8,9,10,19,24,36,42,43,44,45,46,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[6,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,-49,-12,-8,-9,-10,-11,-38,-45,-50,-52,-54,-56,-57,6,-46,-51,-53,-55,6,6,-6,-47,6,6,6,6,6,6,6,6,6,6,6,6,-44,-5,-48,6,6,6,6,6,6,6,6,6,6,6,6,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,6,6,-41,6,-42,6,6,6,6,6,-43,6,6,6,6,6,-28,-29,-30,-31,-32,6,6,6,6,6,6,6,6,6,6,6,6,-17,-19,-21,-18,-20,-22,]),'INT':([0,2,3,4,5,7,8,9,10,19,24,36,42,43,44,45,46,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[10,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,-49,-12,-8,-9,-10,-11,-38,-45,-50,-52,-54,-56,-57,10,-46,-51,-53,-55,10,10,-6,-47,10,10,10,10,10,10,10,10,10,10,10,10,-44,-5,-48,10,10,10,10,10,10,10,10,10,10,10,10,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,10,10,-41,10,-42,10,10,10,10,10,-43,10,10,10,10,10,-28,-29,-30,-31,-32,10,10,10,10,10,10,10,10,10,10,10,10,-17,-19,-21,-18,-20,-22,]),'REAL':([0,2,3,4,5,7,8,9,10,19,24,27,29,36,37,42,43,44,45,46,49,50,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[7,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,40,44,-49,59,-12,-8,-9,-10,-11,72,75,-38,-45,-50,-52,-54,-56,-57,7,-46,-51,-53,-55,7,7,-6,-47,7,7,7,7,7,7,7,7,7,7,7,7,-44,-5,-48,7,7,7,7,7,7,7,7,7,7,7,7,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,7,7,-41,7,-42,7,7,7,7,7,-43,7,7,7,7,7,-28,-29,-30,-31,-32,7,7,7,7,7,7,7,7,7,7,7,7,-17,-19,-21,-18,-20,-22,]),'BOOLEANO':([0,2,3,4,5,7,8,9,10,19,24,29,36,42,43,44,45,46,49,50,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[9,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,46,-49,-12,-8,-9,-10,-11,71,76,-38,-45,-50,-52,-54,-56,-57,9,-46,-51,-53,-55,9,9,-6,-47,9,9,9,9,9,9,9,9,9,9,9,9,-44,-5,-48,9,9,9,9,9,9,9,9,9,9,9,9,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,9,9,-41,9,-42,9,9,9,9,9,-43,9,9,9,9,9,-28,-29,-30,-31,-32,9,9,9,9,9,9,9,9,9,9,9,9,-17,-19,-21,-18,-20,-22,]),'CADEIA_CAR':([0,2,3,4,5,7,8,9,10,19,24,27,29,36,42,43,44,45,46,49,50,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[8,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,37,45,-49,-12,-8,-9,-10,-11,70,77,-38,-45,-50,-52,-54,-56,-57,8,-46,-51,-53,-55,8,8,-6,-47,8,8,8,8,8,8,8,8,8,8,8,8,-44,-5,-48,8,8,8,8,8,8,8,8,8,8,8,8,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,8,8,-41,8,-42,8,8,8,8,8,-43,8,8,8,8,8,-28,-29,-30,-31,-32,8,8,8,8,8,8,8,8,8,8,8,8,-17,-19,-21,-18,-20,-22,]),'PARA':([0,2,3,4,5,7,8,9,10,19,24,36,42,43,44,45,46,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[11,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,-49,-12,-8,-9,-10,-11,-38,-45,-50,-52,-54,-56,-57,11,-46,-51,-53,-55,11,11,-6,-47,11,11,11,11,11,11,11,11,11,11,11,11,-44,-5,-48,11,11,11,11,11,11,11,11,11,11,11,11,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,11,11,-41,11,-42,11,11,11,11,11,-43,11,11,11,11,11,-28,-29,-30,-31,-32,11,11,11,11,11,11,11,11,11,11,11,11,-17,-19,-21,-18,-20,-22,]),'SE':([0,2,3,4,5,7,8,9,10,19,24,36,42,43,44,45,46,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[12,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,-49,-12,-8,-9,-10,-11,-38,-45,-50,-52,-54,-56,-57,12,-46,-51,-53,-55,12,12,-6,-47,12,12,12,12,12,12,12,12,12,12,12,12,-44,-5,-48,12,12,12,12,12,12,12,12,12,12,12,12,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,12,12,-41,12,-42,12,12,12,12,12,-43,12,12,12,12,12,-28,-29,-30,-31,-32,12,12,12,12,12,12,12,12,12,12,12,12,-17,-19,-21,-18,-20,-22,]),'ENQUANTO':([0,2,3,4,5,7,8,9,10,19,24,36,42,43,44,45,46,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[13,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,-49,-12,-8,-9,-10,-11,-38,-45,-50,-52,-54,-56,-57,13,-46,-51,-53,-55,13,13,-6,-47,13,13,13,13,13,13,13,13,13,13,13,13,-44,-5,-48,13,13,13,13,13,13,13,13,13,13,13,13,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,13,13,-41,13,-42,13,13,13,13,13,-43,13,13,13,13,13,-28,-29,-30,-31,-32,13,13,13,13,13,13,13,13,13,13,13,13,-17,-19,-21,-18,-20,-22,]),'RETORNO':([0,2,3,4,5,7,8,9,10,19,24,36,42,43,44,45,46,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[14,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,-49,-12,-8,-9,-10,-11,-38,-45,-50,-52,-54,-56,-57,14,-46,-51,-53,-55,14,14,-6,-47,14,14,14,14,14,14,14,14,14,14,14,14,-44,-5,-48,14,14,14,14,14,14,14,14,14,14,14,14,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,14,14,-41,14,-42,14,14,14,14,14,-43,14,14,14,14,14,-28,-29,-30,-31,-32,14,14,14,14,14,14,14,14,14,14,14,14,-17,-19,-21,-18,-20,-22,]),'FUNK':([0,2,3,4,5,7,8,9,10,19,24,36,42,43,44,45,46,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[15,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,-49,-12,-8,-9,-10,-11,-38,-45,-50,-52,-54,-56,-57,15,-46,-51,-53,-55,15,15,-6,-47,15,15,15,15,15,15,15,15,15,15,15,15,-44,-5,-48,15,15,15,15,15,15,15,15,15,15,15,15,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,15,15,-41,15,-42,15,15,15,15,15,-43,15,15,15,15,15,-28,-29,-30,-31,-32,15,15,15,15,15,15,15,15,15,15,15,15,-17,-19,-21,-18,-20,-22,]),'NOME_FUNK':([0,2,3,4,5,7,8,9,10,15,19,24,36,42,43,44,45,46,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[16,-1,-2,-3,-4,-14,-16,-15,-13,25,-7,-39,-49,-12,-8,-9,-10,-11,-38,-45,-50,-52,-54,-56,-57,16,-46,-51,-53,-55,16,16,-6,-47,16,16,16,16,16,16,16,16,16,16,16,16,-44,-5,-48,16,16,16,16,16,16,16,16,16,16,16,16,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,16,16,-41,16,-42,16,16,16,16,16,-43,16,16,16,16,16,-28,-29,-30,-31,-32,16,16,16,16,16,16,16,16,16,16,16,16,-17,-19,-21,-18,-20,-22,]),'ESCREVA':([0,2,3,4,5,7,8,9,10,19,24,36,42,43,44,45,46,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[17,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,-49,-12,-8,-9,-10,-11,-38,-45,-50,-52,-54,-56,-57,17,-46,-51,-53,-55,17,17,-6,-47,17,17,17,17,17,17,17,17,17,17,17,17,-44,-5,-48,17,17,17,17,17,17,17,17,17,17,17,17,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,17,17,-41,17,-42,17,17,17,17,17,-43,17,17,17,17,17,-28,-29,-30,-31,-32,17,17,17,17,17,17,17,17,17,17,17,17,-17,-19,-21,-18,-20,-22,]),'LEIA':([0,2,3,4,5,7,8,9,10,19,24,36,42,43,44,45,46,51,55,56,60,61,62,63,80,82,83,84,85,102,103,104,106,111,112,113,114,115,116,117,118,119,120,123,124,125,126,127,132,133,134,135,136,137,138,139,140,141,143,144,145,152,153,154,155,156,157,158,159,160,161,162,163,164,176,177,184,185,186,187,188,189,196,197,198,199,200,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,],[18,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,-49,-12,-8,-9,-10,-11,-38,-45,-50,-52,-54,-56,-57,18,-46,-51,-53,-55,18,18,-6,-47,18,18,18,18,18,18,18,18,18,18,18,18,-44,-5,-48,18,18,18,18,18,18,18,18,18,18,18,18,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,18,18,-41,18,-42,18,18,18,18,18,-43,18,18,18,18,18,-28,-29,-30,-31,-32,18,18,18,18,18,18,18,18,18,18,18,18,-17,-19,-21,-18,-20,-22,]),'$end':([1,2,3,4,5,7,8,9,10,19,24,36,42,43,44,45,46,51,55,56,60,61,62,63,82,83,84,85,106,125,127,145,152,153,154,155,156,157,158,159,160,161,164,177,189,207,208,209,210,211,224,225,226,227,228,229,],[0,-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,-49,-12,-8,-9,-10,-11,-38,-45,-50,-52,-54,-56,-57,-46,-51,-53,-55,-47,-44,-48,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,-41,-42,-43,-28,-29,-30,-31,-32,-17,-19,-21,-18,-20,-22,]),'FECHA_CHAV':([2,3,4,5,7,8,9,10,19,24,36,42,43,44,45,46,51,55,56,60,61,62,63,82,83,84,85,103,104,106,124,125,126,127,132,133,134,135,136,137,138,139,140,141,144,145,152,153,154,155,156,157,158,159,160,161,163,164,176,177,189,196,197,198,199,200,207,208,209,210,211,218,219,220,221,222,223,224,225,226,227,228,229,],[-1,-2,-3,-4,-14,-16,-15,-13,-7,-39,-49,-12,-8,-9,-10,-11,-38,-45,-50,-52,-54,-56,-57,-46,-51,-53,-55,125,-6,-47,145,-44,-5,-48,152,153,154,155,156,157,158,159,160,161,164,-40,-23,-24,-25,-26,-27,-33,-34,-35,-36,-37,177,-41,189,-42,-43,207,208,209,210,211,-28,-29,-30,-31,-32,224,225,226,227,228,229,-17,-19,-21,-18,-20,-22,]),'VAR':([6,20,21,22,23,26,27,28,29,34,35,37,47,48,49,50,52,54,78,81,86,87,88,89,100,128,130,131,165,166,167,168,169,170,],[19,30,31,32,33,35,38,41,42,52,54,57,64,66,68,73,78,81,100,105,107,108,109,110,121,146,149,151,178,179,180,181,182,183,]),'ABRE_PAR':([11,12,13,14,16,17,18,25,],[20,21,22,23,26,27,28,34,]),'INTEIRO':([14,27,29,37,47,48,49,50,128,129,130,],[24,39,43,58,65,67,69,74,147,148,150,]),'OPER_ATRIB_IGUAL':([19,30,],[29,47,]),'FECHA_PAR':([26,33,34,35,37,38,39,40,41,52,54,57,58,59,68,69,70,71,72,73,74,75,76,77,78,81,100,105,121,190,191,192,193,194,195,],[36,51,53,55,56,60,61,62,63,79,82,83,84,85,90,91,92,93,94,95,96,97,98,99,101,106,122,127,142,201,202,203,204,205,206,]),'OPER_RELA':([30,31,32,107,108,109,110,],[48,49,50,128,129,130,131,]),'ABRE_CHAV':([53,79,90,91,92,93,94,95,96,97,98,99,101,122,142,171,172,173,174,175,201,202,203,204,205,206,],[80,102,111,112,113,114,115,116,117,118,119,120,123,143,162,184,185,186,187,188,212,213,214,215,216,217,]),'PONTO_VIRG':([64,65,66,67,146,147,148,149,150,151,],[86,87,88,89,165,166,167,168,169,170,]),'SENAO':([152,153,154,155,156,],[171,172,173,174,175,]),'ITERADORES':([178,179,180,181,182,183,],[190,191,192,193,194,195,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'codigo':([0,80,102,103,111,112,113,114,115,116,117,118,119,120,123,124,132,133,134,135,136,137,138,139,140,141,143,144,162,163,176,184,185,186,187,188,196,197,198,199,200,212,213,214,215,216,217,218,219,220,221,222,223,],[1,104,104,126,104,104,104,104,104,104,104,104,104,104,104,126,126,126,126,126,126,126,126,126,126,126,104,126,104,126,126,104,104,104,104,104,126,126,126,126,126,104,104,104,104,104,104,126,126,126,126,126,126,]),'codigos':([80,102,111,112,113,114,115,116,117,118,119,120,123,143,162,184,185,186,187,188,212,213,214,215,216,217,],[103,124,132,133,134,135,136,137,138,139,140,141,144,163,176,196,197,198,199,200,218,219,220,221,222,223,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> codigo","S'",1,None,None,None),
  ('codigo -> IFSULDEMINAS','codigo',1,'p_ifsuldeminas','lex.py',94),
  ('codigo -> COMPILADORES','codigo',1,'p_compiladores','lex.py',97),
  ('codigo -> INICIO','codigo',1,'p_inicio','lex.py',100),
  ('codigo -> FIM','codigo',1,'p_fim','lex.py',103),
  ('codigos -> codigos codigo','codigos',2,'p_codigo_mais','lex.py',106),
  ('codigos -> codigo','codigos',1,'p_codigo_simples','lex.py',109),
  ('codigo -> TIPO VAR','codigo',2,'p_variavel','lex.py',112),
  ('codigo -> TIPO VAR OPER_ATRIB_IGUAL INTEIRO','codigo',4,'p_variavel','lex.py',113),
  ('codigo -> TIPO VAR OPER_ATRIB_IGUAL REAL','codigo',4,'p_variavel','lex.py',114),
  ('codigo -> TIPO VAR OPER_ATRIB_IGUAL CADEIA_CAR','codigo',4,'p_variavel','lex.py',115),
  ('codigo -> TIPO VAR OPER_ATRIB_IGUAL BOOLEANO','codigo',4,'p_variavel','lex.py',116),
  ('codigo -> TIPO VAR OPER_ATRIB_IGUAL VAR','codigo',4,'p_variavel','lex.py',117),
  ('codigo -> INT','codigo',1,'p_tipo','lex.py',121),
  ('codigo -> REAL','codigo',1,'p_tipo','lex.py',122),
  ('codigo -> BOOLEANO','codigo',1,'p_tipo','lex.py',123),
  ('codigo -> CADEIA_CAR','codigo',1,'p_tipo','lex.py',124),
  ('codigo -> PARA ABRE_PAR VAR OPER_ATRIB_IGUAL VAR PONTO_VIRG VAR OPER_RELA VAR PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',16,'p_para','lex.py',128),
  ('codigo -> PARA ABRE_PAR VAR OPER_RELA VAR PONTO_VIRG VAR OPER_RELA VAR PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',16,'p_para','lex.py',129),
  ('codigo -> PARA ABRE_PAR VAR OPER_ATRIB_IGUAL VAR PONTO_VIRG VAR OPER_RELA INTEIRO PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',16,'p_para','lex.py',130),
  ('codigo -> PARA ABRE_PAR VAR OPER_RELA VAR PONTO_VIRG VAR OPER_RELA INTEIRO PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',16,'p_para','lex.py',131),
  ('codigo -> PARA ABRE_PAR VAR OPER_ATRIB_IGUAL INTEIRO PONTO_VIRG VAR OPER_RELA INTEIRO PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',16,'p_para','lex.py',133),
  ('codigo -> PARA ABRE_PAR VAR OPER_RELA INTEIRO PONTO_VIRG VAR OPER_RELA VAR PONTO_VIRG VAR ITERADORES FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',16,'p_para','lex.py',134),
  ('codigo -> SE ABRE_PAR VAR OPER_RELA VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',9,'p_condicional','lex.py',139),
  ('codigo -> SE ABRE_PAR VAR OPER_RELA INTEIRO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',9,'p_condicional','lex.py',140),
  ('codigo -> SE ABRE_PAR VAR OPER_RELA CADEIA_CAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',9,'p_condicional','lex.py',141),
  ('codigo -> SE ABRE_PAR VAR OPER_RELA BOOLEANO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',9,'p_condicional','lex.py',142),
  ('codigo -> SE ABRE_PAR VAR OPER_RELA REAL FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',9,'p_condicional','lex.py',143),
  ('codigo -> SE ABRE_PAR VAR OPER_RELA VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV SENAO ABRE_CHAV codigos FECHA_CHAV','codigo',13,'p_condicional','lex.py',145),
  ('codigo -> SE ABRE_PAR VAR OPER_RELA INTEIRO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV SENAO ABRE_CHAV codigos FECHA_CHAV','codigo',13,'p_condicional','lex.py',146),
  ('codigo -> SE ABRE_PAR VAR OPER_RELA CADEIA_CAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV SENAO ABRE_CHAV codigos FECHA_CHAV','codigo',13,'p_condicional','lex.py',147),
  ('codigo -> SE ABRE_PAR VAR OPER_RELA BOOLEANO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV SENAO ABRE_CHAV codigos FECHA_CHAV','codigo',13,'p_condicional','lex.py',148),
  ('codigo -> SE ABRE_PAR VAR OPER_RELA REAL FECHA_PAR ABRE_CHAV codigos FECHA_CHAV SENAO ABRE_CHAV codigos FECHA_CHAV','codigo',13,'p_condicional','lex.py',149),
  ('codigo -> ENQUANTO ABRE_PAR VAR OPER_RELA VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',9,'p_enquanto','lex.py',154),
  ('codigo -> ENQUANTO ABRE_PAR VAR OPER_RELA INTEIRO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',9,'p_enquanto','lex.py',155),
  ('codigo -> ENQUANTO ABRE_PAR VAR OPER_RELA REAL FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',9,'p_enquanto','lex.py',156),
  ('codigo -> ENQUANTO ABRE_PAR VAR OPER_RELA BOOLEANO FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',9,'p_enquanto','lex.py',157),
  ('codigo -> ENQUANTO ABRE_PAR VAR OPER_RELA CADEIA_CAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',9,'p_enquanto','lex.py',158),
  ('codigo -> RETORNO ABRE_PAR VAR FECHA_PAR','codigo',4,'p_retorno','lex.py',162),
  ('codigo -> RETORNO INTEIRO','codigo',2,'p_retorno','lex.py',163),
  ('codigo -> FUNK NOME_FUNK ABRE_PAR VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',8,'p_definir_funk','lex.py',167),
  ('codigo -> FUNK NOME_FUNK ABRE_PAR VAR VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',9,'p_definir_funk','lex.py',168),
  ('codigo -> FUNK NOME_FUNK ABRE_PAR VAR VAR VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',10,'p_definir_funk','lex.py',169),
  ('codigo -> FUNK NOME_FUNK ABRE_PAR VAR VAR VAR VAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',11,'p_definir_funk','lex.py',170),
  ('codigo -> FUNK NOME_FUNK ABRE_PAR FECHA_PAR ABRE_CHAV codigos FECHA_CHAV','codigo',7,'p_definir_funk','lex.py',171),
  ('codigo -> NOME_FUNK ABRE_PAR VAR FECHA_PAR','codigo',4,'p_chamar_funk','lex.py',175),
  ('codigo -> NOME_FUNK ABRE_PAR VAR VAR FECHA_PAR','codigo',5,'p_chamar_funk','lex.py',176),
  ('codigo -> NOME_FUNK ABRE_PAR VAR VAR VAR FECHA_PAR','codigo',6,'p_chamar_funk','lex.py',177),
  ('codigo -> NOME_FUNK ABRE_PAR VAR VAR VAR VAR FECHA_PAR','codigo',7,'p_chamar_funk','lex.py',178),
  ('codigo -> NOME_FUNK ABRE_PAR FECHA_PAR','codigo',3,'p_chamar_funk','lex.py',179),
  ('codigo -> ESCREVA ABRE_PAR CADEIA_CAR FECHA_PAR','codigo',4,'p_escreva','lex.py',183),
  ('codigo -> ESCREVA ABRE_PAR CADEIA_CAR VAR FECHA_PAR','codigo',5,'p_escreva','lex.py',184),
  ('codigo -> ESCREVA ABRE_PAR VAR FECHA_PAR','codigo',4,'p_escreva','lex.py',185),
  ('codigo -> ESCREVA ABRE_PAR CADEIA_CAR INTEIRO FECHA_PAR','codigo',5,'p_escreva','lex.py',186),
  ('codigo -> ESCREVA ABRE_PAR INTEIRO FECHA_PAR','codigo',4,'p_escreva','lex.py',187),
  ('codigo -> ESCREVA ABRE_PAR CADEIA_CAR REAL FECHA_PAR','codigo',5,'p_escreva','lex.py',188),
  ('codigo -> ESCREVA ABRE_PAR REAL FECHA_PAR','codigo',4,'p_escreva','lex.py',189),
  ('codigo -> LEIA ABRE_PAR VAR FECHA_PAR','codigo',4,'p_leia','lex.py',194),
]