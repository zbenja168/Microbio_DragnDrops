BRICK = {
    "brick_num": 4,
    "brick_title": "Principles of Antibacterial Drugs",
    "games": [
        {
            "slug": "mic_mbc_concepts",
            "title": "MIC, MBC, and Killing Power",
            "subtitle": "Match each core concept to its definition, how it is determined, and its clinical significance",
            "categories": ["Definition", "How It Is Determined or Classified", "Clinical Significance"],
            "data": {
                "MIC": {
                    "Definition": "Minimal antibiotic concentration that inhibits bacterial growth",
                    "How It Is Determined or Classified": "Lowest dilution with no visible turbidity in the mixture",
                    "Clinical Significance": "Standard susceptibility measure; assays return in about 24 hours"
                },
                "MBC": {
                    "Definition": "Minimum concentration resulting in bacterial cell death",
                    "How It Is Determined or Classified": "Concentration giving a 99.9% reduction in colony count",
                    "Clinical Significance": "Rarely obtained in practice outside of research"
                },
                "Breakpoint": {
                    "Definition": "Cutoff MIC considered susceptible for an organism-antibiotic pair",
                    "How It Is Determined or Classified": "Closely monitored and published by a national organization",
                    "Clinical Significance": "Underlies susceptibility calls on lab reports that guide therapy"
                },
                "Bacteriostatic agents": {
                    "Definition": "Agents that halt bacterial growth and replication",
                    "How It Is Determined or Classified": "MBC to MIC ratio greater than 4",
                    "Clinical Significance": "Immunocompetent host more easily clears the halted organism"
                },
                "Bactericidal agents": {
                    "Definition": "Agents whose primary action is actually killing bacteria",
                    "How It Is Determined or Classified": "MBC to MIC ratio of 4 or less",
                    "Clinical Significance": "Preferred for endocarditis, meningitis, and immunosuppressed patients"
                }
            }
        },
        {
            "slug": "pkpd_ratios",
            "title": "Three Ways to Beat the MIC",
            "subtitle": "Match each PK/PD ratio to its definition, the drugs or role it applies to, and its practical impact",
            "categories": ["What the Ratio Compares", "Example Drugs or Role", "Dosing or Classification Impact"],
            "data": {
                "T > MIC": {
                    "What the Ratio Compares": "Duration the drug concentration stays above the MIC",
                    "Example Drugs or Role": "Penicillins, cephalosporins, carbapenems, monobactams",
                    "Dosing or Classification Impact": "Time-dependent: more frequent dosing, three or four times daily"
                },
                "Cmax / MIC": {
                    "What the Ratio Compares": "Peak drug concentration relative to the MIC",
                    "Example Drugs or Role": "Fluoroquinolones, aminoglycosides, metronidazole, daptomycin",
                    "Dosing or Classification Impact": "Concentration-dependent: larger doses given once daily"
                },
                "AUC / MIC": {
                    "What the Ratio Compares": "Area under the concentration-time curve over the MIC",
                    "Example Drugs or Role": "Vancomycin, macrolides, tetracyclines, linezolid",
                    "Dosing or Classification Impact": "Best activity predictor for both -cidal and -static agents"
                },
                "MBC / MIC": {
                    "What the Ratio Compares": "Killing concentration relative to inhibitory concentration",
                    "Example Drugs or Role": "Decides if a drug is bacteriostatic or bactericidal",
                    "Dosing or Classification Impact": "Ratio of 4 or less is -cidal; greater than 4 is -static"
                }
            }
        },
        {
            "slug": "class_activity_pkpd",
            "title": "Class, Activity, and Parameter",
            "subtitle": "Match each drug class to its antibacterial activity and its predictive PK/PD parameter",
            "categories": ["Antibacterial Activity", "Predictive PK/PD Parameter"],
            "data": {
                "Penicillins": {
                    "Antibacterial Activity": "Bactericidal",
                    "Predictive PK/PD Parameter": "Time > MIC"
                },
                "Vancomycin": {
                    "Antibacterial Activity": "Bactericidal (slow)",
                    "Predictive PK/PD Parameter": "AUC / MIC"
                },
                "Fluoroquinolones": {
                    "Antibacterial Activity": "Bactericidal",
                    "Predictive PK/PD Parameter": "Cmax / MIC"
                },
                "Metronidazole": {
                    "Antibacterial Activity": "Bactericidal",
                    "Predictive PK/PD Parameter": "Cmax / MIC"
                },
                "Tetracyclines": {
                    "Antibacterial Activity": "Bacteriostatic",
                    "Predictive PK/PD Parameter": "AUC / MIC"
                },
                "Linezolid": {
                    "Antibacterial Activity": "Bacteriostatic",
                    "Predictive PK/PD Parameter": "AUC / MIC"
                }
            }
        },
        {
            "slug": "empiric_to_definitive",
            "title": "From Best Guess to Best Choice",
            "subtitle": "Match each therapy tool to what it is, how it is used, and its key detail",
            "categories": ["What It Is", "When or How It Is Used", "Key Detail"],
            "data": {
                "Empiric therapy": {
                    "What It Is": "'Best guess' antibiotics covering likely and dangerous culprits",
                    "When or How It Is Used": "Started before culture and susceptibility results return",
                    "Key Detail": "Weighs disease process, common pathogens, local resistance rates"
                },
                "Definitive therapy": {
                    "What It Is": "Best antibiotic choice for the identified organism",
                    "When or How It Is Used": "Chosen with clinical judgement once susceptibility is known",
                    "Key Detail": "Often a de-escalation from broader initial coverage"
                },
                "Antibiogram": {
                    "What It Is": "Profile of how susceptible organisms are to a range of drugs",
                    "When or How It Is Used": "Guides empiric choices from local resistance patterns",
                    "Key Detail": "Aggregate facility data over a defined time frame"
                },
                "Culture and sensitivity report": {
                    "What It Is": "Patient-specific report marking antibiotics S, I, or R",
                    "When or How It Is Used": "Converts empiric therapy into definitive therapy",
                    "Key Detail": "Built from MIC testing of the patient's own sample"
                }
            }
        }
    ]
}
