BRICK = {
    "brick_num": 38,
    "brick_title": "Antiretrovirals — Drugs to Treat and Prevent HIV Infection",
    "games": [
        {
            "slug": "class_mechanisms",
            "title": "Antiretroviral Classes: Mechanisms",
            "subtitle": "Match each drug class to its viral target, mechanism, and role in therapy",
            "categories": ["Viral target", "Mechanism", "Role in therapy"],
            "data": {
                "NRTIs": {
                    "Viral target": "Reverse transcriptase (RNA-to-DNA step)",
                    "Mechanism": "Chain terminators incorporated into the growing nucleotide chain",
                    "Role in therapy": "Mainstay of treatment; two form the backbone of initial regimens"
                },
                "NNRTIs": {
                    "Viral target": "Reverse transcriptase, bound directly",
                    "Mechanism": "Bind and inactivate the enzyme, stopping DNA chain polymerization",
                    "Role in therapy": "Most common class made ineffective by resistance in the US"
                },
                "Integrase strand transfer inhibitors": {
                    "Viral target": "Integrase enzyme",
                    "Mechanism": "Block insertion of HIV DNA into the host cell genome",
                    "Role in therapy": "Most common third drug added to two NRTIs initially"
                },
                "Protease inhibitors": {
                    "Viral target": "Protease enzyme",
                    "Mechanism": "Stop cutting of polyprotein chains into mature HIV units",
                    "Role in therapy": "Considered when a patient fails initial antiretroviral therapy"
                },
                "Entry/fusion inhibitors": {
                    "Viral target": "CCR5 receptor or gp41",
                    "Mechanism": "Prevent binding and fusion so the virus cannot enter the cell",
                    "Role in therapy": "Sometimes useful for drug-resistant virus infection"
                }
            }
        },
        {
            "slug": "named_drugs",
            "title": "Name That Antiretroviral",
            "subtitle": "Match each drug to its class and its signature mechanism or key fact",
            "categories": ["Class or role", "Mechanism / key fact"],
            "data": {
                "Maraviroc": {
                    "Class or role": "Entry inhibitor",
                    "Mechanism / key fact": "Blocks CCR5 so the virus cannot bind and enter the cell"
                },
                "Enfuvirtide": {
                    "Class or role": "Fusion inhibitor",
                    "Mechanism / key fact": "Binds gp41, exposed once HIV binds gp120, blocking fusion"
                },
                "Ritonavir": {
                    "Class or role": "Protease inhibitor used as a booster",
                    "Mechanism / key fact": "Inhibits hepatic CYP450 to raise protease inhibitor levels"
                },
                "Cobicistat": {
                    "Class or role": "Pharmacokinetic enhancer",
                    "Mechanism / key fact": "CYP450 inhibitor that lowers dosing frequency, aiding adherence"
                },
                "Efavirenz": {
                    "Class or role": "NNRTI",
                    "Mechanism / key fact": "Induces CYP450 and may decrease levels of bictegravir"
                },
                "Elvitegravir": {
                    "Class or role": "Integrase strand transfer inhibitor",
                    "Mechanism / key fact": "The INSTI that may require pharmacokinetic boosting"
                }
            }
        },
        {
            "slug": "adverse_effects",
            "title": "Antiretroviral Toxicities",
            "subtitle": "Match each drug to its class, hallmark adverse effect, and lecture detail",
            "categories": ["Class", "Hallmark adverse effect", "Lecture detail"],
            "data": {
                "Tenofovir DF": {
                    "Class": "NRTI derived from adenosine",
                    "Hallmark adverse effect": "Kidney injury and bone loss",
                    "Lecture detail": "TAF form has far fewer of these effects and is preferred"
                },
                "Zidovudine": {
                    "Class": "NRTI derived from thymidine",
                    "Hallmark adverse effect": "Bone marrow suppression with neutropenia",
                    "Lecture detail": "Formerly known as AZT"
                },
                "Didanosine": {
                    "Class": "NRTI",
                    "Hallmark adverse effect": "Pancreatitis",
                    "Lecture detail": "Rarely used because of the risk of complications"
                },
                "Abacavir": {
                    "Class": "NRTI derived from guanosine",
                    "Hallmark adverse effect": "Unique hypersensitivity reaction",
                    "Lecture detail": "Every HIV-positive patient must be tested for HLA-B*5701"
                },
                "Efavirenz": {
                    "Class": "NNRTI",
                    "Hallmark adverse effect": "CNS toxicity and QT prolongation",
                    "Lecture detail": "Also monitor for increases in hepatic enzymes"
                },
                "Atazanavir": {
                    "Class": "Protease inhibitor",
                    "Hallmark adverse effect": "Nephrotoxicity",
                    "Lecture detail": "Ritonavir boosting may limit these adverse effects"
                }
            }
        },
        {
            "slug": "prophylaxis_strategies",
            "title": "Preventing HIV and Its Complications",
            "subtitle": "Match each prevention strategy to when it is used and what is given",
            "categories": ["When it is used", "What is given"],
            "data": {
                "Postexposure prophylaxis (PEP)": {
                    "When it is used": "Health care worker after accidental exposure like a needlestick",
                    "What is given": "Three-drug regimen; stopped if the source tests noninfected"
                },
                "Nonoccupational PEP (nPEP)": {
                    "When it is used": "Unprotected sex or percutaneous blood exposure outside work",
                    "What is given": "Antiretroviral therapy started within 72 hours of exposure"
                },
                "Preexposure prophylaxis (PrEP)": {
                    "When it is used": "High-risk groups: IV drug users, sex workers, MSM",
                    "What is given": "Antiretroviral combo plus education and condom use"
                },
                "P jiroveci pneumonia prophylaxis": {
                    "When it is used": "CD4 count below 200/mm3",
                    "What is given": "Trimethoprim-sulfamethoxazole (TMP-SMX)"
                },
                "Toxoplasmosis prophylaxis": {
                    "When it is used": "CD4 count below 100/mm3",
                    "What is given": "TMP-SMX, same agent as for P jiroveci"
                },
                "Mycobacterium avium complex prophylaxis": {
                    "When it is used": "CD4 count below 50/mm3",
                    "What is given": "Azithromycin, though new guidelines say ART alone may suffice"
                }
            }
        }
    ]
}
