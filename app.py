import streamlit as st

##############################################################################
# 1) UKMEC CATEGORY DEFINITIONS
##############################################################################
CATEGORY_DEFINITIONS = {
    1: (
        "UKMEC 1: A condition for which there is no restriction "
        "for the use of the method."
    ),
    2: (
        "UKMEC 2: A condition where the advantages of using the method "
        "generally outweigh the theoretical or proven risks."
    ),
    3: (
        "UKMEC 3: A condition where the theoretical or proven risks "
        "usually outweigh the advantages of using the method. "
        "Use of the method requires expert clinical judgement and/or referral "
        "to a specialist, since the method is not usually recommended unless "
        "other more appropriate methods are not available or not acceptable."
    ),
    4: (
        "UKMEC 4: A condition which represents an unacceptable health risk "
        "if the method is used."
    ),
}

INITIATION_DEFINITION = (
    "**Initiation (I)** = Starting the method by a woman who has a specific medical condition."
)
CONTINUATION_DEFINITION = (
    "**Continuation (C)** = Continuing the method already in use when a woman "
    "develops a new medical condition."
)

METHODS = [
    "Cu-IUD",
    "LNG-IUS",
    "IMP",
    "DMPA",
    "POP",
    "CHC",
    "Female Sterilization"
]

##############################################################################
# 2) GIANT UKMEC DATA DICTIONARY
##############################################################################
# Each key is a unique condition code (e.g. "BREASTFEEDING_0_TO_6_WEEKS").
# The value is a dict: {method: (initiation_cat, continuation_cat), ...} for all 7 methods.
# 
# Transcribed from the final UKMEC summary table plus postpartum/abortion postpartum expansions, etc.
# 
# We store (I, C) even if they are the same, for consistency.

UKMEC_DATA = {

    # ---------------------------------------------------------------------
    # PERSONAL CHARACTERISTICS & REPRODUCTIVE HISTORY
    # ---------------------------------------------------------------------
    # Age
    "AGE_MENARCHE_TO_LT_20": {
        "Cu-IUD": (2,2), "LNG-IUS": (2,2), "IMP": (1,1), "DMPA": (2,2),
        "POP": (1,1), "CHC": (1,1), "Female Sterilization": (1,1),
    },
    "AGE_GE_20": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (1,1), "Female Sterilization": (1,1),
    },

    # Parity
    "PARITY_NULLIPAROUS": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (1,1), "Female Sterilization": (1,1),
    },
    "PARITY_PAROUS": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (1,1), "Female Sterilization": (1,1),
    },

    # Breastfeeding: 0 to <6 weeks
    "BREASTFEEDING_0_TO_6_WEEKS": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (2,2), "DMPA": (1,1),
        "POP": (4,4), "CHC": (4,4), "Female Sterilization": (1,1),
    },
    # Breastfeeding: ≥6 weeks to <6 months (primarily BF)
    "BREASTFEEDING_6_WEEKS_TO_6_MONTHS": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (2,2), "CHC": (2,2), "Female Sterilization": (1,1),
    },
    # Breastfeeding: ≥6 months
    "BREASTFEEDING_GE_6_MONTHS": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (1,1), "Female Sterilization": (1,1),
    },

    # Postpartum (non-bf), 0 to <3 weeks + risk factors for VTE
    "PP_0_TO_3_WEEKS_VTE": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (2,2), "DMPA": (1,1),
        "POP": (4,4), "CHC": (4,4), "Female Sterilization": (1,1),
    },
    # Postpartum (non-bf), 0 to <3 weeks NO VTE
    "PP_0_TO_3_WEEKS_NO_VTE": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (2,2), "DMPA": (1,1),
        "POP": (3,3), "CHC": (3,3), "Female Sterilization": (1,1),
    },
    # Postpartum (non-bf), 3 to <6 weeks + VTE
    "PP_3_TO_6_WEEKS_VTE": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (2,2), "DMPA": (1,1),
        "POP": (3,3), "CHC": (3,3), "Female Sterilization": (1,1),
    },
    # Postpartum (non-bf), 3 to <6 weeks NO VTE
    "PP_3_TO_6_WEEKS_NO_VTE": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (2,2), "CHC": (2,2), "Female Sterilization": (1,1),
    },
    # Postpartum (non-bf), ≥6 weeks
    "PP_GE_6_WEEKS": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (1,1), "Female Sterilization": (1,1),
    },

    # Postpartum IUC insertion:
    "PP_0_TO_48H_IUC": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (None,None), "DMPA": (None,None),
        "POP": (None,None), "CHC": (None,None), "Female Sterilization": (None,None),
    },
    "PP_48H_TO_4W_IUC": {
        "Cu-IUD": (3,3), "LNG-IUS": (3,3), "IMP": (None,None), "DMPA": (None,None),
        "POP": (None,None), "CHC": (None,None), "Female Sterilization": (None,None),
    },
    "PP_SEPSIS": {
        "Cu-IUD": (4,4), "LNG-IUS": (4,4), "IMP": (None,None), "DMPA": (None,None),
        "POP": (None,None), "CHC": (None,None), "Female Sterilization": (None,None),
    },

    # Post-abortion
    "ABORT_1ST_TRIM": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (1,1), "Female Sterilization": (1,1),
    },
    "ABORT_2ND_TRIM": {
        "Cu-IUD": (2,2), "LNG-IUS": (2,2), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (1,1), "Female Sterilization": (1,1),
    },
    "ABORT_SEPSIS": {
        "Cu-IUD": (4,4), "LNG-IUS": (4,4), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (1,1), "Female Sterilization": (1,1),
    },

    # Past ectopic
    "PAST_ECTOPIC": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (1,1), "Female Sterilization": (1,1),
    },

    # History pelvic surgery => all 1
    "HX_PELVIC_SURG": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (1,1), "Female Sterilization": (1,1),
    },

    # Smoking
    "SMOKE_AGE_LT_35": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (2,2), "Female Sterilization": (1,1),
    },
    "SMOKE_AGE_GE_35_LT15": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (3,3), "Female Sterilization": (1,1),
    },
    "SMOKE_AGE_GE_35_GE15": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (4,4), "Female Sterilization": (1,1),
    },
    "SMOKE_AGE_GE_35_STOP_LT1": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (3,3), "Female Sterilization": (1,1),
    },
    "SMOKE_AGE_GE_35_STOP_GE1": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (2,2), "Female Sterilization": (1,1),
    },

    # Obesity (BMI)
    "OBESITY_BMI_30_34": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (2,2), "Female Sterilization": (1,1),
    },
    "OBESITY_BMI_GE_35": {
        "Cu-IUD": (1,1), "LNG-IUS": (1,1), "IMP": (1,1), "DMPA": (1,1),
        "POP": (1,1), "CHC": (3,3), "Female Sterilization": (1,1),
    },

    # ---------------------------------------------------------------------
    # ORGAN TRANSPLANT, CARDIO, HTN, etc. (Skipping comment, just listing)
    # ---------------------------------------------------------------------
    "TRANSPLANT_COMPLICATED": {
        "Cu-IUD": (2,2),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (3,3),
        "POP": (2,2),"CHC": (3,3),"Female Sterilization": (2,2),
    },
    "TRANSPLANT_UNCOMPLICATED": {
        "Cu-IUD": (2,2),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (2,2),"Female Sterilization": (2,2),
    },

    "CVD_MULTIPLE_RISK": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (3,3),
        "POP": (2,2),"CHC": (3,3),"Female Sterilization": (1,1),
    },

    # Hypertension
    "HTN_ADEQ_CONTROL": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (2,2),
        "POP": (1,1),"CHC": (3,3),"Female Sterilization": (1,1),
    },
    "HTN_SYST_140_159_DIA_90_99": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (3,3),"Female Sterilization": (1,1),
    },
    "HTN_SYST_GE160_DIA_GE100": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (2,2),
        "POP": (1,1),"CHC": (4,4),"Female Sterilization": (1,1),
    },
    "HTN_VASC_DISEASE": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (3,3),
        "POP": (2,2),"CHC": (4,4),"Female Sterilization": (1,1),
    },
    "HX_HIGH_BP_PREG": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (2,2),"Female Sterilization": (1,1),
    },

    "IHD_CURRENT_OR_HISTORY": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (3,3),
        "POP": (2,2),"CHC": (4,4),"Female Sterilization": (1,1),
    },
    "STROKE_TIA": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (3,3),
        "POP": (2,2),"CHC": (4,4),"Female Sterilization": (1,1),
    },

    "DYSLIPIDEMIAS": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (2,2),"Female Sterilization": (1,1),
    },

    # VTE
    "VTE_HISTORY": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (4,4),"Female Sterilization": (1,1),
    },
    "VTE_CURRENT_ANTICOAG": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (4,4),"Female Sterilization": (1,1),
    },
    "VTE_FHX_1ST_LT_45": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (3,3),"Female Sterilization": (1,1),
    },
    "VTE_FHX_1ST_GE_45": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (2,2),"Female Sterilization": (1,1),
    },
    "VTE_MAJ_SURG_PROLONG_IMMOB": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (4,4),"Female Sterilization": (1,1),
    },
    "VTE_MAJ_SURG_NO_IMMOB": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (2,2),"Female Sterilization": (1,1),
    },
    "VTE_MINOR_SURG_NO_IMMOB": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "VTE_IMMOBILITY": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (3,3),"Female Sterilization": (1,1),
    },
    "SVT_VARICOSE": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "SVT_THROMBOSIS": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (2,2),"Female Sterilization": (1,1),
    },
    "THROMBO_MUTATIONS": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (4,4),"Female Sterilization": (1,1),
    },

    # Valvular / Congenital
    "VALV_CONG_UNCOMPLICATED": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (2,2),"Female Sterilization": (1,1),
    },
    "VALV_CONG_COMPLICATED": {
        "Cu-IUD": (2,2),"LNG-IUS": (2,2),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (4,4),"Female Sterilization": (2,2),
    },

    # Cardiomyopathy
    "CARDIOMYO_NORMAL": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (2,2),"Female Sterilization": (1,1),
    },
    "CARDIOMYO_IMPAIRED": {
        "Cu-IUD": (2,2),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (4,4),"Female Sterilization": (2,2),
    },

    # Arrhythmias
    "AF": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (4,4),"Female Sterilization": (1,1),
    },
    "LONG_QT": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (1,1),"DMPA": (2,2),
        "POP": (1,1),"CHC": (2,2),"Female Sterilization": (1,1),
    },

    # NEURO
    "HEADACHE_NON_MIGRAINE": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (2,2),"Female Sterilization": (1,1),
    },
    "MIGRAINE_NO_AURA": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (1,1),"CHC": (3,3),"Female Sterilization": (1,1),
    },
    "MIGRAINE_WITH_AURA": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (4,4),"Female Sterilization": (1,1),
    },
    "MIGRAINE_AURA_HX_5Y": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (3,3),"Female Sterilization": (1,1),
    },
    "IIH": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (2,2),"Female Sterilization": (1,1),
    },
    "EPILEPSY": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },

    "DEPRESSION": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },

    # BREAST & REPRO TRACT
    # Vaginal bleeding
    "BLEED_IRREG_NO_HEAVY": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "BLEED_HEAVY_OR_PROLONGED": {
        "Cu-IUD": (2,2),"LNG-IUS": (1,1),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "UNEXPL_BLEED_BEFORE_EVAL": {
        "Cu-IUD": (4,2),"LNG-IUS": (4,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (2,2),"Female Sterilization": (2,2),
    },

    "ENDOMETRIOSIS": {
        "Cu-IUD": (2,2),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "OVARIAN_BENIGN": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "DYSMENORRHEA_SEV": {
        "Cu-IUD": (2,2),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },

    # GTD
    "GTD_UNDETECTABLE_HCG": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "GTD_DECREASING_HCG": {
        "Cu-IUD": (3,3),"LNG-IUS": (3,3),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (3,3),
    },
    "GTD_PERSIST_ELEV": {
        "Cu-IUD": (4,4),"LNG-IUS": (4,4),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (4,4),
    },

    "CERVICAL_ECTROPION": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "CIN": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (1,1),"DMPA": (2,2),
        "POP": (1,1),"CHC": (2,2),"Female Sterilization": (1,1),
    },
    # Cervical Ca
    "CERV_CA_AWAIT_TX_I": {
        "Cu-IUD": (2,2),"LNG-IUS": (2,2),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (2,2),"Female Sterilization": (2,2),
    },
    "CERV_CA_AWAIT_TX_C": {
        "Cu-IUD": (4,4),"LNG-IUS": (4,4),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (2,2),"Female Sterilization": (4,4),
    },
    "CERV_CA_RAD_TRA": {
        "Cu-IUD": (3,3),"LNG-IUS": (3,3),"IMP": (2,2),"DMPA": (2,2),
        "POP": (1,1),"CHC": (2,2),"Female Sterilization": (3,3),
    },

    # Breast conditions
    "BREAST_UNDX_MASS_I": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (3,3),"Female Sterilization": (1,1),
    },
    "BREAST_UNDX_MASS_C": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (2,2),"Female Sterilization": (1,1),
    },
    "BREAST_BENIGN": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "BREAST_FHX_CA": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "BREAST_BRCA_MUT": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (3,3),"Female Sterilization": (1,1),
    },
    "BREAST_CA_CURRENT": {
        "Cu-IUD": (1,1),"LNG-IUS": (4,4),"IMP": (4,4),"DMPA": (4,4),
        "POP": (4,4),"CHC": (4,4),"Female Sterilization": (1,1),
    },
    "BREAST_CA_PAST": {
        "Cu-IUD": (1,1),"LNG-IUS": (3,3),"IMP": (3,3),"DMPA": (3,3),
        "POP": (3,3),"CHC": (3,3),"Female Sterilization": (1,1),
    },

    "ENDOMETRIAL_CA_I": {
        "Cu-IUD": (1,4),"LNG-IUS": (1,2),"IMP": (1,2),"DMPA": (1,2),
        "POP": (1,2),"CHC": (1,2),"Female Sterilization": (1,4),
    },
    "ENDOMETRIAL_CA_C": {
        # some are from the doc: "4,2" or "2,2", we interpret carefully
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (2,2),"Female Sterilization": (2,2),
    },

    "OVARIAN_CA": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },

    "FIBROIDS_NO_DISTORT": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "FIBROIDS_DISTORT": {
        "Cu-IUD": (3,3),"LNG-IUS": (3,3),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (3,3),
    },
    "ANAT_UTERINE_DISTORT": {
        "Cu-IUD": (3,3),"LNG-IUS": (3,3),"IMP": (None,None),"DMPA": (None,None),
        "POP": (None,None),"CHC": (None,None),"Female Sterilization": (3,3),
    },
    "ANAT_UTERINE_OTHER": {
        "Cu-IUD": (2,2),"LNG-IUS": (2,2),"IMP": (None,None),"DMPA": (None,None),
        "POP": (None,None),"CHC": (None,None),"Female Sterilization": (2,2),
    },

    # PID
    "PID_PAST_NO_RISK": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "PID_CURRENT_I": {
        "Cu-IUD": (4,4),"LNG-IUS": (4,4),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (4,4),
    },
    "PID_CURRENT_C": {
        "Cu-IUD": (2,2),"LNG-IUS": (2,2),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (2,2),
    },

    # STIs
    "STI_CHLAM_SYMPT_I": {
        "Cu-IUD": (4,4),"LNG-IUS": (4,4),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (4,4),
    },
    "STI_CHLAM_SYMPT_C": {
        "Cu-IUD": (2,2),"LNG-IUS": (2,2),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (2,2),
    },
    "STI_CHLAM_ASYMP_I": {
        "Cu-IUD": (3,3),"LNG-IUS": (3,3),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (3,3),
    },
    "STI_CHLAM_ASYMP_C": {
        "Cu-IUD": (2,2),"LNG-IUS": (2,2),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (2,2),
    },
    "STI_GONORR_I": {
        "Cu-IUD": (4,4),"LNG-IUS": (4,4),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (4,4),
    },
    "STI_GONORR_C": {
        "Cu-IUD": (2,2),"LNG-IUS": (2,2),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (2,2),
    },
    "STI_OTHER_CURRENT": {
        "Cu-IUD": (2,2),"LNG-IUS": (2,2),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (2,2),
    },
    "STI_VAGINITIS": {
        "Cu-IUD": (2,2),"LNG-IUS": (2,2),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (2,2),
    },
    "STI_INCREASED_RISK": {
        "Cu-IUD": (2,2),"LNG-IUS": (2,2),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (2,2),
    },

    # HIV
    "HIV_HIGH_RISK": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "HIV_INF_CD4_GE200": {
        "Cu-IUD": (2,2),"LNG-IUS": (2,2),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (2,2),
    },
    "HIV_INF_CD4_LT200_I": {
        "Cu-IUD": (3,3),"LNG-IUS": (3,3),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (3,3),
    },
    "HIV_INF_CD4_LT200_C": {
        "Cu-IUD": (2,2),"LNG-IUS": (2,2),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (2,2),
    },

    # TB
    "TB_NON_PELVIC": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "TB_PELVIC_I": {
        "Cu-IUD": (4,4),"LNG-IUS": (4,4),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (4,4),
    },
    "TB_PELVIC_C": {
        "Cu-IUD": (3,3),"LNG-IUS": (3,3),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (3,3),
    },

    # ENDOCRINE: Diabetes
    "DM_GESTATIONAL": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "DM_NON_VASC_NON_INSULIN": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (2,2),"Female Sterilization": (1,1),
    },
    "DM_NON_VASC_INSULIN": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (2,2),"Female Sterilization": (1,1),
    },
    "DM_NEURO_RETINO": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (3,3),"Female Sterilization": (1,1),
    },
    "DM_OTHER_VASC": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (3,3),"Female Sterilization": (1,1),
    },

    # Viral hepatitis
    "HEP_ACUTE_FLARE_I": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (3,3),"Female Sterilization": (1,1),
    },
    "HEP_ACUTE_FLARE_C": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (2,2),"Female Sterilization": (1,1),
    },
    "HEP_CARRIER": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "HEP_CHRONIC": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },

    # Cirrhosis
    "CIRRHOSIS_MILD": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (1,1),
    },
    "CIRRHOSIS_SEVERE": {
        "Cu-IUD": (1,1),"LNG-IUS": (3,3),"IMP": (3,3),"DMPA": (3,3),
        "POP": (3,3),"CHC": (4,4),"Female Sterilization": (1,1),
    },

    # Liver tumours
    "LIVER_BENIGN_FNH": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (2,2),"Female Sterilization": (1,1),
    },
    "LIVER_BENIGN_HCA": {
        "Cu-IUD": (1,1),"LNG-IUS": (3,3),"IMP": (3,3),"DMPA": (3,3),
        "POP": (3,3),"CHC": (4,4),"Female Sterilization": (1,1),
    },
    "LIVER_MALIGNANT": {
        "Cu-IUD": (1,1),"LNG-IUS": (3,3),"IMP": (3,3),"DMPA": (3,3),
        "POP": (3,3),"CHC": (4,4),"Female Sterilization": (1,1),
    },

    "IBD": {
        "Cu-IUD": (1,1),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (2,2),"CHC": (2,2),"Female Sterilization": (1,1),
    },

    # Anaemias
    "THALASSAEMIA": {
        "Cu-IUD": (2,2),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (2,2),
    },
    "SICKLE_CELL": {
        "Cu-IUD": (2,2),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (2,2),"Female Sterilization": (2,2),
    },
    "IRON_DEF_ANAEMIA": {
        "Cu-IUD": (2,2),"LNG-IUS": (1,1),"IMP": (1,1),"DMPA": (1,1),
        "POP": (1,1),"CHC": (1,1),"Female Sterilization": (2,2),
    },

    # Rheumatic
    "RA": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (2,2),"Female Sterilization": (1,1),
    },
    "SLE_NO_APL": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (2,2),"Female Sterilization": (1,1),
    },
    "SLE_APL": {
        "Cu-IUD": (1,1),"LNG-IUS": (2,2),"IMP": (2,2),"DMPA": (2,2),
        "POP": (2,2),"CHC": (4,4),"Female Sterilization": (1,1),
    },

    # Done: We have a massive dictionary covering all final summary table conditions.
}

##############################################################################
# 3) HELPER: COMBINE MULTIPLE CONDITIONS
##############################################################################
def combine_ukmec_categories(
    chosen_method: str,
    chosen_conditions: list[str],
    is_initiation: bool
) -> int:
    """
    For the chosen method, gather the (I, C) category from each condition.
    We pick the worst (max) category among them all.

    If a condition's dictionary for that method is None, we skip it.
    If it doesn't exist, we skip it.
    """
    if chosen_method not in METHODS:
        st.warning(f"Unknown method: {chosen_method}")
        return 1

    final_cat = 1
    index = 0 if is_initiation else 1
    for cond_key in chosen_conditions:
        if cond_key not in UKMEC_DATA:
            # not in dictionary at all
            continue
        method_map = UKMEC_DATA[cond_key]
        if chosen_method not in method_map:
            continue
        cat_tuple = method_map[chosen_method]
        if cat_tuple is None:
            # means that row didn't apply or is N/A
            continue
        cat_value = cat_tuple[index]  # the (I or C) category
        if cat_value is not None:
            final_cat = max(final_cat, cat_value)

    return final_cat

##############################################################################
# 4) STREAMLIT APP
##############################################################################
def main():
    st.title("Comprehensive UKMEC Contraception Checker (All Conditions)")

    st.markdown("""
    This single-page app includes **all** conditions from the 2016 UKMEC final summary table.
    It demonstrates a *wizard-like* approach, though we present all conditions in checkboxes here.
    
    **Steps**:
    1. Review Category definitions and 'Initiation (I)' vs. 'Continuation (C)'.
    2. Enter basic info (age, postpartum, etc.).
    3. Select your chosen contraceptive method.
    4. Indicate whether it's for Initiation or Continuation.
    5. Mark any relevant conditions from the massive list below.
    6. We'll compute the *worst* (maximum) category for that method.
    ---
    """)

    # Show category definitions
    st.subheader("UKMEC Categories")
    for k,v in CATEGORY_DEFINITIONS.items():
        st.write(f"**Category {k}**: {v}")

    st.subheader("Initiation vs. Continuation")
    st.markdown(f"- {INITIATION_DEFINITION}")
    st.markdown(f"- {CONTINUATION_DEFINITION}")

    st.info("Please proceed with the form below.")

    # Basic info
    st.header("Step 1: Basic Info")
    age = st.number_input("Age (years)", min_value=10, max_value=60, value=25)

    st.header("Step 2: Contraceptive Method Selection")
    chosen_method = st.selectbox("Which method?",
        METHODS
    )

    st.header("Step 3: Initiation vs. Continuation")
    init_cont = st.radio("Pick one:", ["Initiation", "Continuation"])
    is_initiation = (init_cont == "Initiation")

    st.header("Step 4: Select all relevant conditions below")

    # We'll store condition keys in a list
    chosen_conditions = []

    # We'll group the checkboxes by broad categories:
    st.subheader("A) Personal Characteristics & Reproductive History")
    if st.checkbox("Age <20"):
        chosen_conditions.append("AGE_MENARCHE_TO_LT_20")
    else:
        chosen_conditions.append("AGE_GE_20")

    if st.checkbox("Nulliparous?"):
        chosen_conditions.append("PARITY_NULLIPAROUS")
    else:
        chosen_conditions.append("PARITY_PAROUS")

    postpartum = st.checkbox("Is postpartum?")
    if postpartum:
        bf = st.checkbox("Breastfeeding?")
        weeks_pp = st.number_input("Weeks postpartum", 0.0, 52.0, 2.0)
        # user picks checkboxes for VTE risk etc. For brevity, 
        # we'll do a simplified approach:
        vte_risk = st.checkbox("Other VTE risk factors postpartum?")

        if bf:
            if weeks_pp < 6:
                chosen_conditions.append("BREASTFEEDING_0_TO_6_WEEKS")
            elif 6 <= weeks_pp < 24:  # ~6 months
                chosen_conditions.append("BREASTFEEDING_6_WEEKS_TO_6_MONTHS")
            else:
                chosen_conditions.append("BREASTFEEDING_GE_6_MONTHS")
        else:
            if weeks_pp < 3:
                if vte_risk:
                    chosen_conditions.append("PP_0_TO_3_WEEKS_VTE")
                else:
                    chosen_conditions.append("PP_0_TO_3_WEEKS_NO_VTE")
            elif 3 <= weeks_pp < 6:
                if vte_risk:
                    chosen_conditions.append("PP_3_TO_6_WEEKS_VTE")
                else:
                    chosen_conditions.append("PP_3_TO_6_WEEKS_NO_VTE")
            else:
                chosen_conditions.append("PP_GE_6_WEEKS")

        if st.checkbox("Postpartum sepsis?"):
            chosen_conditions.append("PP_SEPSIS")

    abortion = st.checkbox("Had abortion <24 weeks?")
    if abortion:
        tri = st.radio("Trimester of abortion", ["1st","2nd"])
        if tri=="1st":
            chosen_conditions.append("ABORT_1ST_TRIM")
        else:
            chosen_conditions.append("ABORT_2ND_TRIM")

        if st.checkbox("Post-abortion sepsis?"):
            chosen_conditions.append("ABORT_SEPSIS")

    if st.checkbox("Past ectopic pregnancy?"):
        chosen_conditions.append("PAST_ECTOPIC")

    # Smoking
    st.subheader("B) Smoking")
    smokes = st.checkbox("Smoker?")
    if smokes:
        if age < 35:
            chosen_conditions.append("SMOKE_AGE_LT_35")
        else:
            # how many cigs
            cigs = st.number_input("Cigarettes/day (≥0)", 0, 60, 10)
            if cigs == 0:
                st.write("Ex-smoker => how long since stopped?")
                stopped = st.radio("Stopped <1yr or ≥1yr?", ["<1yr", "≥1yr"])
                if stopped == "<1yr":
                    chosen_conditions.append("SMOKE_AGE_GE_35_STOP_LT1")
                else:
                    chosen_conditions.append("SMOKE_AGE_GE_35_STOP_GE1")
            elif cigs < 15:
                chosen_conditions.append("SMOKE_AGE_GE_35_LT15")
            else:
                chosen_conditions.append("SMOKE_AGE_GE_35_GE15")

    # BMI
    st.subheader("C) Obesity (BMI)")
    bmi = st.number_input("BMI", 10.0, 70.0, 25.0)
    if 30 <= bmi < 35:
        chosen_conditions.append("OBESITY_BMI_30_34")
    elif bmi >= 35:
        chosen_conditions.append("OBESITY_BMI_GE_35")

    # We'll let the user manually pick from the rest of the giant list:
    st.subheader("D) Medical Conditions (check all that apply)")

    # We'll create lumps of checkboxes for each major heading:
    # This is tedious, but it ensures the user can pick all conditions if needed.

    # 1) Organ transplant
    if st.checkbox("Complicated organ transplant?"):
        chosen_conditions.append("TRANSPLANT_COMPLICATED")
    if st.checkbox("Uncomplicated organ transplant?"):
        chosen_conditions.append("TRANSPLANT_UNCOMPLICATED")

    # 2) Hypertension / CVD
    if st.checkbox("Multiple CVD risk factors?"):
        chosen_conditions.append("CVD_MULTIPLE_RISK")
    if st.checkbox("Hypertension, adequately controlled?"):
        chosen_conditions.append("HTN_ADEQ_CONTROL")
    if st.checkbox("HTN: 140-159/90-99?"):
        chosen_conditions.append("HTN_SYST_140_159_DIA_90_99")
    if st.checkbox("HTN: ≥160/≥100?"):
        chosen_conditions.append("HTN_SYST_GE160_DIA_GE100")
    if st.checkbox("HTN w/ vascular disease?"):
        chosen_conditions.append("HTN_VASC_DISEASE")
    if st.checkbox("History of high BP in pregnancy?"):
        chosen_conditions.append("HX_HIGH_BP_PREG")
    if st.checkbox("Ischaemic heart disease (current/past)?"):
        chosen_conditions.append("IHD_CURRENT_OR_HISTORY")
    if st.checkbox("Stroke / TIA (current/past)?"):
        chosen_conditions.append("STROKE_TIA")
    if st.checkbox("Known dyslipidaemias?"):
        chosen_conditions.append("DYSLIPIDEMIAS")

    # 3) VTE
    if st.checkbox("History of VTE?"):
        chosen_conditions.append("VTE_HISTORY")
    if st.checkbox("Current VTE (on anticoagulants)?"):
        chosen_conditions.append("VTE_CURRENT_ANTICOAG")
    if st.checkbox("Family history VTE <45?"):
        chosen_conditions.append("VTE_FHX_1ST_LT_45")
    if st.checkbox("Family history VTE ≥45?"):
        chosen_conditions.append("VTE_FHX_1ST_GE_45")
    if st.checkbox("Major surgery w/ prolonged immobilization?"):
        chosen_conditions.append("VTE_MAJ_SURG_PROLONG_IMMOB")
    if st.checkbox("Major surgery w/o prolonged immobilization?"):
        chosen_conditions.append("VTE_MAJ_SURG_NO_IMMOB")
    if st.checkbox("Minor surgery w/o immobilization?"):
        chosen_conditions.append("VTE_MINOR_SURG_NO_IMMOB")
    if st.checkbox("Chronic immobility (wheelchair, etc.)?"):
        chosen_conditions.append("VTE_IMMOBILITY")
    if st.checkbox("Superficial varicose veins?"):
        chosen_conditions.append("SVT_VARICOSE")
    if st.checkbox("Superficial venous thrombosis?"):
        chosen_conditions.append("SVT_THROMBOSIS")
    if st.checkbox("Known thrombogenic mutations?"):
        chosen_conditions.append("THROMBO_MUTATIONS")

    # 4) Valvular/congenital heart disease
    if st.checkbox("Valvular/CHD (uncomplicated)?"):
        chosen_conditions.append("VALV_CONG_UNCOMPLICATED")
    if st.checkbox("Valvular/CHD (complicated)?"):
        chosen_conditions.append("VALV_CONG_COMPLICATED")

    # 5) Cardiomyopathy / arrhythmias
    if st.checkbox("Cardiomyopathy with normal function?"):
        chosen_conditions.append("CARDIOMYO_NORMAL")
    if st.checkbox("Cardiomyopathy with impaired function?"):
        chosen_conditions.append("CARDIOMYO_IMPAIRED")
    if st.checkbox("Atrial fibrillation?"):
        chosen_conditions.append("AF")
    if st.checkbox("Known Long QT syndrome?"):
        chosen_conditions.append("LONG_QT")

    # 6) Neuro
    if st.checkbox("Non-migrainous headache?"):
        chosen_conditions.append("HEADACHE_NON_MIGRAINE")
    if st.checkbox("Migraine without aura?"):
        chosen_conditions.append("MIGRAINE_NO_AURA")
    if st.checkbox("Migraine with aura?"):
        chosen_conditions.append("MIGRAINE_WITH_AURA")
    if st.checkbox("History of migraine with aura >5 years ago?"):
        chosen_conditions.append("MIGRAINE_AURA_HX_5Y")
    if st.checkbox("Idiopathic intracranial hypertension?"):
        chosen_conditions.append("IIH")
    if st.checkbox("Epilepsy?"):
        chosen_conditions.append("EPILEPSY")

    if st.checkbox("Depression?"):
        chosen_conditions.append("DEPRESSION")

    # 7) Breast & Reproductive
    if st.checkbox("Irregular bleeding (not heavy)?"):
        chosen_conditions.append("BLEED_IRREG_NO_HEAVY")
    if st.checkbox("Heavy/prolonged bleeding?"):
        chosen_conditions.append("BLEED_HEAVY_OR_PROLONGED")
    if st.checkbox("Unexplained bleeding (before evaluation)?"):
        chosen_conditions.append("UNEXPL_BLEED_BEFORE_EVAL")
    if st.checkbox("Endometriosis?"):
        chosen_conditions.append("ENDOMETRIOSIS")
    if st.checkbox("Benign ovarian tumors/cysts?"):
        chosen_conditions.append("OVARIAN_BENIGN")
    if st.checkbox("Severe dysmenorrhea?"):
        chosen_conditions.append("DYSMENORRHEA_SEV")

    # GTD
    if st.checkbox("GTD with undetectable hCG?"):
        chosen_conditions.append("GTD_UNDETECTABLE_HCG")
    if st.checkbox("GTD with decreasing hCG?"):
        chosen_conditions.append("GTD_DECREASING_HCG")
    if st.checkbox("GTD with persistently elevated hCG?"):
        chosen_conditions.append("GTD_PERSIST_ELEV")

    if st.checkbox("Cervical ectropion?"):
        chosen_conditions.append("CERVICAL_ECTROPION")
    if st.checkbox("CIN?"):
        chosen_conditions.append("CIN")

    # Cervical Ca
    if st.checkbox("Cervical Ca awaiting treatment (I)?"):
        chosen_conditions.append("CERV_CA_AWAIT_TX_I")
    if st.checkbox("Cervical Ca awaiting treatment (C)?"):
        chosen_conditions.append("CERV_CA_AWAIT_TX_C")
    if st.checkbox("Cervical Ca radical trachelectomy?"):
        chosen_conditions.append("CERV_CA_RAD_TRA")

    # Breast conditions
    if st.checkbox("Undiagnosed breast mass (I)?"):
        chosen_conditions.append("BREAST_UNDX_MASS_I")
    if st.checkbox("Undiagnosed breast mass (C)?"):
        chosen_conditions.append("BREAST_UNDX_MASS_C")
    if st.checkbox("Benign breast conditions?"):
        chosen_conditions.append("BREAST_BENIGN")
    if st.checkbox("Family history of breast cancer?"):
        chosen_conditions.append("BREAST_FHX_CA")
    if st.checkbox("BRCA gene mutation carrier?"):
        chosen_conditions.append("BREAST_BRCA_MUT")
    if st.checkbox("Current breast cancer?"):
        chosen_conditions.append("BREAST_CA_CURRENT")
    if st.checkbox("Past breast cancer?"):
        chosen_conditions.append("BREAST_CA_PAST")

    # Endometrial Ca
    if st.checkbox("Endometrial Ca (initiation)?"):
        chosen_conditions.append("ENDOMETRIAL_CA_I")
    if st.checkbox("Endometrial Ca (continuation)?"):
        chosen_conditions.append("ENDOMETRIAL_CA_C")

    if st.checkbox("Ovarian Ca?"):
        chosen_conditions.append("OVARIAN_CA")

    if st.checkbox("Fibroids (no distortion)?"):
        chosen_conditions.append("FIBROIDS_NO_DISTORT")
    if st.checkbox("Fibroids (distorting uterine cavity)?"):
        chosen_conditions.append("FIBROIDS_DISTORT")
    # etc. We also have anatomical abnormalities
    if st.checkbox("Anatomical abnormality that distorts uterine cavity?"):
        chosen_conditions.append("ANAT_UTERINE_DISTORT")
    if st.checkbox("Other anatomical abnormality?"):
        chosen_conditions.append("ANAT_UTERINE_OTHER")

    # PID
    if st.checkbox("Past PID (no current risk)?"):
        chosen_conditions.append("PID_PAST_NO_RISK")
    if st.checkbox("Current PID (I)?"):
        chosen_conditions.append("PID_CURRENT_I")
    if st.checkbox("Current PID (C)?"):
        chosen_conditions.append("PID_CURRENT_C")

    # STIs
    if st.checkbox("Chlamydia symptomatic (I)?"):
        chosen_conditions.append("STI_CHLAM_SYMPT_I")
    if st.checkbox("Chlamydia symptomatic (C)?"):
        chosen_conditions.append("STI_CHLAM_SYMPT_C")
    if st.checkbox("Chlamydia asymptomatic (I)?"):
        chosen_conditions.append("STI_CHLAM_ASYMP_I")
    if st.checkbox("Chlamydia asymptomatic (C)?"):
        chosen_conditions.append("STI_CHLAM_ASYMP_C")
    if st.checkbox("Gonorrhea (I)?"):
        chosen_conditions.append("STI_GONORR_I")
    if st.checkbox("Gonorrhea (C)?"):
        chosen_conditions.append("STI_GONORR_C")
    if st.checkbox("Other current STIs?"):
        chosen_conditions.append("STI_OTHER_CURRENT")
    if st.checkbox("Vaginitis?"):
        chosen_conditions.append("STI_VAGINITIS")
    if st.checkbox("Increased risk of STIs?"):
        chosen_conditions.append("STI_INCREASED_RISK")

    # HIV
    if st.checkbox("High risk of HIV infection?"):
        chosen_conditions.append("HIV_HIGH_RISK")
    if st.checkbox("HIV infected, CD4≥200?"):
        chosen_conditions.append("HIV_INF_CD4_GE200")
    if st.checkbox("HIV infected, CD4<200 (I)?"):
        chosen_conditions.append("HIV_INF_CD4_LT200_I")
    if st.checkbox("HIV infected, CD4<200 (C)?"):
        chosen_conditions.append("HIV_INF_CD4_LT200_C")

    # TB
    if st.checkbox("TB (non-pelvic)?"):
        chosen_conditions.append("TB_NON_PELVIC")
    if st.checkbox("TB (pelvic) - Initiation?"):
        chosen_conditions.append("TB_PELVIC_I")
    if st.checkbox("TB (pelvic) - Continuation?"):
        chosen_conditions.append("TB_PELVIC_C")

    # Diabetes
    if st.checkbox("Gestational diabetes history?"):
        chosen_conditions.append("DM_GESTATIONAL")
    if st.checkbox("Diabetes, non-vascular, non-insulin?"):
        chosen_conditions.append("DM_NON_VASC_NON_INSULIN")
    if st.checkbox("Diabetes, non-vascular, insulin?"):
        chosen_conditions.append("DM_NON_VASC_INSULIN")
    if st.checkbox("Diabetic nephropathy/retinopathy?"):
        chosen_conditions.append("DM_NEURO_RETINO")
    if st.checkbox("Other vascular diabetes?"):
        chosen_conditions.append("DM_OTHER_VASC")

    # Hepatitis
    if st.checkbox("Acute or flare hepatitis (I)?"):
        chosen_conditions.append("HEP_ACUTE_FLARE_I")
    if st.checkbox("Acute or flare hepatitis (C)?"):
        chosen_conditions.append("HEP_ACUTE_FLARE_C")
    if st.checkbox("Hepatitis carrier?"):
        chosen_conditions.append("HEP_CARRIER")
    if st.checkbox("Chronic hepatitis?"):
        chosen_conditions.append("HEP_CHRONIC")

    # Cirrhosis
    if st.checkbox("Mild (compensated) cirrhosis?"):
        chosen_conditions.append("CIRRHOSIS_MILD")
    if st.checkbox("Severe (decompensated) cirrhosis?"):
        chosen_conditions.append("CIRRHOSIS_SEVERE")

    # Liver tumors
    if st.checkbox("Benign liver tumor (focal nodular hyperplasia)?"):
        chosen_conditions.append("LIVER_BENIGN_FNH")
    if st.checkbox("Benign hepatocellular adenoma?"):
        chosen_conditions.append("LIVER_BENIGN_HCA")
    if st.checkbox("Malignant liver tumor?"):
        chosen_conditions.append("LIVER_MALIGNANT")

    # IBD
    if st.checkbox("Inflammatory bowel disease?"):
        chosen_conditions.append("IBD")

    # Anaemias
    if st.checkbox("Thalassaemia?"):
        chosen_conditions.append("THALASSAEMIA")
    if st.checkbox("Sickle cell disease?"):
        chosen_conditions.append("SICKLE_CELL")
    if st.checkbox("Iron deficiency anaemia?"):
        chosen_conditions.append("IRON_DEF_ANAEMIA")

    # Rheumatic
    if st.checkbox("Rheumatoid arthritis?"):
        chosen_conditions.append("RA")
    if st.checkbox("SLE, no antiphospholipid antibodies?"):
        chosen_conditions.append("SLE_NO_APL")
    if st.checkbox("SLE with antiphospholipid antibodies?"):
        chosen_conditions.append("SLE_APL")

    st.markdown("----")
    st.write("**Chosen condition keys**:", chosen_conditions)

    # 5) Compute final category
    final_category = combine_ukmec_categories(
        chosen_method, chosen_conditions, is_initiation
    )

    # 6) Display final
    st.header("Result: UKMEC Category")
    st.write(f"For **{chosen_method}** under **{init_cont}**, your final category is: **{final_category}**")
    st.write(CATEGORY_DEFINITIONS[final_category])

    st.warning("""
        This code uses a simple 'maximum category' approach. If multiple Category 2 or 3 
        conditions overlap for the same risk factor, you may need to escalate further.
        Always compare with official guidelines and use clinical judgment.
    """)


if __name__ == "__main__":
    main()
