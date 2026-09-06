BRICK = {
    "brick_num": 8,
    "brick_title": "Carbapenems",
    "games": [
        {
            "slug": "beta_lactam_mechanism",
            "title": "How Carbapenems Kill Bacteria",
            "subtitle": "Match each player in the mechanism to its identity and its role",
            "categories": ["What it is", "Role in killing bacteria"],
            "data": {
                "Beta-lactam ring": {
                    "What it is": "Core structure shared by penicillins, cephalosporins, carbapenems, and monobactams",
                    "Role in killing bacteria": "Mimics D-Ala-D-Ala and binds the transpeptidase enzyme"
                },
                "Transpeptidase (PBP)": {
                    "What it is": "Enzyme that cross-links the linear peptidoglycan chains",
                    "Role in killing bacteria": "Irreversibly, noncompetitively inhibited, so cell wall synthesis halts"
                },
                "Autolysins": {
                    "What it is": "Bacterial autolytic enzymes activated by beta-lactam antibiotics",
                    "Role in killing bacteria": "Cause lesions in the cell wall, leading to osmotic death"
                },
                "Peptidoglycan cell wall": {
                    "What it is": "Meshwork of NAG and NAM chains outside the plasma membrane",
                    "Role in killing bacteria": "Its blocked cross-linking is what kills the bacterium"
                },
                "Rapid bacterial growth": {
                    "What it is": "Active multiplication that requires new cell wall construction",
                    "Role in killing bacteria": "Required for the bactericidal effect of these antibiotics"
                }
            }
        },
        {
            "slug": "spectrum_and_niche",
            "title": "Spectrum and Clinical Niche",
            "subtitle": "Match each agent or combination to its coverage note and clinical niche",
            "categories": ["Coverage note", "Clinical niche"],
            "data": {
                "Carbapenems (class)": {
                    "Coverage note": "Gram-positive cocci, gram-negative rods, anaerobes; some cover Pseudomonas",
                    "Clinical niche": "Last-resort drugs of choice for ESBL-producing organisms"
                },
                "Meropenem/vaborbactam": {
                    "Coverage note": "Vaborbactam blocks beta-lactamases that would inactivate the antibiotic",
                    "Clinical niche": "Expensive; specifically reserved for very resistant organisms"
                },
                "Imipenem/cilastatin/relebactam": {
                    "Coverage note": "Relebactam extends the spectrum against carbapenemase-producing organisms",
                    "Clinical niche": "Imipenem coformulation for organisms producing carbapenemases"
                },
                "IV aztreonam": {
                    "Coverage note": "Monobactam that retains coverage against many ESBL producers",
                    "Clinical niche": "Severe penicillin allergy, since cross-reactivity is not a concern"
                },
                "Inhaled aztreonam": {
                    "Coverage note": "Helps against multi-drug resistant respiratory infections",
                    "Clinical niche": "Reserved for patients with cystic fibrosis"
                }
            }
        },
        {
            "slug": "imipenem_cilastatin_story",
            "title": "The Imipenem-Cilastatin Story",
            "subtitle": "Match each piece of the imipenem puzzle to what it is and what follows",
            "categories": ["What it is", "Consequence"],
            "data": {
                "Renal dipeptidase": {
                    "What it is": "Enzyme in the brush border of the proximal tubule",
                    "Consequence": "Rapidly hydrolyzes imipenem after it is administered"
                },
                "Imipenem given alone": {
                    "What it is": "IV carbapenem with no dipeptidase inhibitor on board",
                    "Consequence": "Essentially ineffective because hydrolysis greatly reduces its half-life"
                },
                "Cilastatin": {
                    "What it is": "Inhibitor of the renal tubular dipeptidase",
                    "Consequence": "Extends imipenem's elimination half-life"
                },
                "Imipenem/cilastatin combination": {
                    "What it is": "Formulated pair with pharmacokinetics like other carbapenems",
                    "Consequence": "Penetrates tissues and cerebrospinal fluid; eliminated in urine"
                },
                "Unadjusted renal impairment": {
                    "What it is": "Poor kidney clearance without a lowered dose",
                    "Consequence": "Drug accumulates, making side effects much more likely"
                }
            }
        },
        {
            "slug": "adverse_effects_interactions",
            "title": "Adverse Effects and Interactions",
            "subtitle": "Match each adverse effect or interaction to its key detail and highest-risk setting",
            "categories": ["Key detail", "Highest-risk setting"],
            "data": {
                "Seizures": {
                    "Key detail": "Carbapenems lower the seizure threshold, especially at higher doses",
                    "Highest-risk setting": "Imipenem/cilastatin, particularly with unadjusted renal impairment"
                },
                "Valproic acid interaction": {
                    "Key detail": "Carbapenems decrease serum valproic acid concentrations",
                    "Highest-risk setting": "Patients with a history of seizures or epilepsy"
                },
                "DRESS / severe skin reaction": {
                    "Key detail": "Drug reaction with eosinophilia and systemic symptoms",
                    "Highest-risk setting": "Rare, but carried across the carbapenem class"
                },
                "Bone marrow suppression": {
                    "Key detail": "Thrombocytopenia and neutropenia with prolonged use",
                    "Highest-risk setting": "Immunosuppressed patients needing long carbapenem courses"
                },
                "Common GI effects": {
                    "Key detail": "Diarrhea, nausea, vomiting, and increased liver function tests",
                    "Highest-risk setting": "The most frequent reactions with carbapenems and monobactams alike"
                }
            }
        }
    ]
}
