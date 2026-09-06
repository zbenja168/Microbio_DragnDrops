BRICK = {
    "brick_num": 42,
    "brick_title": "Antivirals 2 of 2 — Drugs to Treat Influenza and RSV Infection",
    "games": [
        {
            "slug": "know_your_antiviral",
            "title": "Know Your Antiviral",
            "subtitle": "Match each drug to its class, mechanism, and clinical role",
            "categories": ["Drug class", "Mechanism of action", "Clinical role"],
            "data": {
                "Oseltamivir": {
                    "Drug class": "Neuraminidase inhibitor",
                    "Mechanism of action": "Slows spread of newly formed viruses to healthy cells",
                    "Clinical role": "Oral agent; current drug of choice for influenza"
                },
                "Zanamivir": {
                    "Drug class": "Neuraminidase inhibitor, like oseltamivir",
                    "Mechanism of action": "Blocks the enzyme that releases budding virions from cell membranes",
                    "Clinical role": "Inhaled aerosol powder option for influenza"
                },
                "Ribavirin": {
                    "Drug class": "Guanosine analog; guanine nucleotide synthesis inhibitor",
                    "Mechanism of action": "Mimics purine, joins the growing nucleic acid strand, halts elongation",
                    "Clinical role": "Only drug used for RSV; also treats hepatitis C"
                },
                "Amantadine and rimantadine": {
                    "Drug class": "M2 ion channel blockers",
                    "Mechanism of action": "Block the viral M2 ion channel",
                    "Clinical role": "Formerly for influenza; abandoned due to high resistance rates"
                }
            }
        },
        {
            "slug": "toxicity_traceback",
            "title": "Toxicity Traceback",
            "subtitle": "Match each adverse effect to its culprit drug and the key clinical point",
            "categories": ["Culprit drug", "Key clinical point"],
            "data": {
                "Hemolytic anemia": {
                    "Culprit drug": "Ribavirin",
                    "Key clinical point": "FDA black box warning; anemia can stress the heart and trigger MI"
                },
                "Teratogenicity": {
                    "Culprit drug": "Ribavirin (pregnancy category X)",
                    "Key clinical point": "Proven teratogen; contraindicated in pregnant patients"
                },
                "Nausea, vomiting, and GI upset": {
                    "Culprit drug": "Oseltamivir",
                    "Key clinical point": "Adverse effects track with its oral route of administration"
                },
                "Airway irritation and sore throat": {
                    "Culprit drug": "Zanamivir",
                    "Key clinical point": "Expected from an inhaled aerosol powder"
                },
                "Neutropenia": {
                    "Culprit drug": "Ribavirin given with interferon alpha",
                    "Key clinical point": "Reported with concurrent interferon use in hepatitis C regimens"
                }
            }
        },
        {
            "slug": "place_in_therapy",
            "title": "Who Gets What?",
            "subtitle": "Match each patient scenario to the best management and the lecture's rationale",
            "categories": ["Best management", "Rationale"],
            "data": {
                "Hospitalized patient with severe influenza": {
                    "Best management": "Neuraminidase inhibitor antiviral therapy",
                    "Rationale": "Guidelines recommend antivirals for severe influenza requiring hospitalization"
                },
                "Healthy adult whose flu began over 48 hours ago": {
                    "Best management": "Supportive care; antiviral adds nothing now",
                    "Rationale": "Past 48 hours the virus is barely budding, so inhibitors are ineffective"
                },
                "Severely immunocompromised transplant patient with RSV": {
                    "Best management": "Consider ribavirin, carefully individualized",
                    "Rationale": "The only RSV patients in whom antiviral therapy is indicated"
                },
                "RSV with wheezing and underlying asthma or COPD": {
                    "Best management": "Bronchodilators and steroids for symptom relief",
                    "Rationale": "Helps lower respiratory tract symptoms in reactive airway disease"
                },
                "Adult over 60 with risk factors, or pregnant": {
                    "Best management": "RSV vaccine, FDA approved May 2023",
                    "Rationale": "Has significantly reduced RSV infections in these vulnerable populations"
                }
            }
        },
        {
            "slug": "resistance_and_interactions",
            "title": "Resistance and Interactions",
            "subtitle": "Match each scenario to what happens and the clinical takeaway",
            "categories": ["What happens", "Clinical takeaway"],
            "data": {
                "H275Y neuraminidase mutation": {
                    "What happens": "Histidine changes to tyrosine at amino acid 275",
                    "Clinical takeaway": "Confers resistance to oseltamivir"
                },
                "Live influenza virus vaccine near antiviral therapy": {
                    "What happens": "Antivirals may diminish the vaccine's therapeutic effect",
                    "Clinical takeaway": "Avoid vaccine within 2 weeks before or 48 hours after antivirals"
                },
                "Warfarin in a patient starting ribavirin": {
                    "What happens": "Ribavirin may diminish the vitamin K antagonist's anticoagulant effect",
                    "Clinical takeaway": "Increase warfarin dose or use alternate anticoagulation during the course"
                },
                "Circulating influenza strains with neuraminidase mutations": {
                    "What happens": "Mutations directly reduce inhibition of the neuraminidase enzyme",
                    "Clinical takeaway": "Resistance can arise with or without drug exposure; most strains stay susceptible"
                }
            }
        }
    ]
}
