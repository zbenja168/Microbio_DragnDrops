BRICK = {
    "brick_num": 10,
    "brick_title": "Penicillins",
    "games": [
        {
            "slug": "penicillin_classes",
            "title": "Penicillin Subgroups",
            "subtitle": "Match each penicillin class to its example drugs, spectrum, and beta-lactamase story",
            "categories": ["Example Drugs", "Spectrum of Activity", "Beta-Lactamase Note"],
            "data": {
                "Natural Penicillins": {
                    "Example Drugs": "Penicillin G and penicillin V",
                    "Spectrum of Activity": "Greatest activity against gram-positive cocci and rods",
                    "Beta-Lactamase Note": "Susceptible to hydrolysis by beta-lactamases"
                },
                "Antistaphylococcal Penicillins": {
                    "Example Drugs": "Nafcillin, oxacillin, cloxacillin",
                    "Spectrum of Activity": "Active against staphylococci and streptococci; limited spectrum",
                    "Beta-Lactamase Note": "Resistant to staphylococcal beta-lactamases"
                },
                "Aminopenicillins": {
                    "Example Drugs": "Ampicillin and amoxicillin",
                    "Spectrum of Activity": "Extended coverage; increased stability to gastric acid",
                    "Beta-Lactamase Note": "Coformulated with clavulanate or sulbactam to extend activity"
                },
                "Antipseudomonal Penicillins": {
                    "Example Drugs": "Piperacillin with tazobactam",
                    "Spectrum of Activity": "Broadest: improved gram-positive and gram-negative activity",
                    "Beta-Lactamase Note": "Tazobactam coformulation covers serious Pseudomonas infections"
                }
            }
        },
        {
            "slug": "drug_pk_profiles",
            "title": "Drug-by-Drug Pharmacokinetics",
            "subtitle": "Match each penicillin to its subgroup and its absorption or excretion quirk",
            "categories": ["Subgroup", "Pharmacokinetic Fact"],
            "data": {
                "Penicillin G": {
                    "Subgroup": "Natural penicillin",
                    "Pharmacokinetic Fact": "Poorly absorbed orally; broken down by gastric acid"
                },
                "Penicillin V": {
                    "Subgroup": "Natural penicillin with better oral absorption",
                    "Pharmacokinetic Fact": "Increased absorption due to increased acid stability"
                },
                "Nafcillin": {
                    "Subgroup": "Antistaphylococcal penicillin",
                    "Pharmacokinetic Fact": "Poor oral absorption; mainly excreted in the bile"
                },
                "Ampicillin": {
                    "Subgroup": "Aminopenicillin available parenterally",
                    "Pharmacokinetic Fact": "Undergoes enterohepatic recycling"
                },
                "Piperacillin": {
                    "Subgroup": "Antipseudomonal derivative of ampicillin",
                    "Pharmacokinetic Fact": "Polar injectable compound; not metabolized extensively"
                },
                "Most penicillins overall": {
                    "Subgroup": "Beta-lactams sharing the core two-ring structure",
                    "Pharmacokinetic Fact": "Excreted unchanged in urine; half-life 30 minutes to 1 hour"
                }
            }
        },
        {
            "slug": "adverse_reactions",
            "title": "Adverse Reactions to Penicillins",
            "subtitle": "Match each reaction to its mechanism and clinical presentation",
            "categories": ["Mechanism", "Clinical Presentation"],
            "data": {
                "Type 1 hypersensitivity": {
                    "Mechanism": "IgE on mast cells binds metabolites; histamine release",
                    "Clinical Presentation": "Within 2-20 minutes: hives, bronchoconstriction, hypotension, wheezing"
                },
                "Type 2 hypersensitivity": {
                    "Mechanism": "IgG reacts with penicillin absorbed on red blood cells",
                    "Clinical Presentation": "Coombs-positive hemolytic anemia after prolonged high-dose IV therapy"
                },
                "Type 3 hypersensitivity": {
                    "Mechanism": "Circulating antibody-antigen complexes deposit in tissues",
                    "Clinical Presentation": "Serum sickness 1-3 weeks after starting: urticaria, lymphadenopathy, arthralgia"
                },
                "Type 4 hypersensitivity": {
                    "Mechanism": "Delayed reaction causing drug-induced tubular interstitial nephritis",
                    "Clinical Presentation": "Fever, eosinophilia, rash, and hematuria"
                },
                "Jarisch-Herxheimer reaction": {
                    "Mechanism": "Killed spirochetes release toxins during penicillin G therapy",
                    "Clinical Presentation": "Flu-like fever, chills, and headache in treated syphilis"
                },
                "Ampicillin or amoxicillin rash": {
                    "Mechanism": "Non-allergic maculopapular eruption; risk rises with infectious mononucleosis",
                    "Clinical Presentation": "Small flat discolored spots and raised papules"
                }
            }
        },
        {
            "slug": "mechanism_and_resistance",
            "title": "Kill Mechanisms vs Resistance Moves",
            "subtitle": "Match each concept to how it works and its key detail from the brick",
            "categories": ["How It Works", "Key Detail"],
            "data": {
                "Cross-link inhibition": {
                    "How It Works": "Beta-lactam ring mimics D-Ala-D-Ala, irreversibly binding transpeptidase",
                    "Key Detail": "Halted cell wall synthesis kills only rapidly growing bacteria"
                },
                "Autolysin activation": {
                    "How It Works": "Beta-lactams trigger wall enzymes that digest the cell wall",
                    "Key Detail": "Autolysins sit predominantly in gram-positive bacteria; osmotic death"
                },
                "Beta-lactamase production": {
                    "How It Works": "Bacterial enzyme cleaves the beta-lactam ring, ending activity",
                    "Key Detail": "Major resistance mechanism in gram-positives and gram-negatives alike"
                },
                "PBP mutation": {
                    "How It Works": "Structural change in the target protein reduces drug binding",
                    "Key Detail": "Seen in resistant S. pneumoniae and methicillin-resistant staphylococci"
                },
                "Porin alteration": {
                    "How It Works": "Changed outer-wall channels impede penicillin access to PBPs",
                    "Key Detail": "Minor mechanism in gram-negative rods like Pseudomonas aeruginosa"
                },
                "Beta-lactamase inhibitors": {
                    "How It Works": "Coformulated agents protect the beta-lactam ring from cleavage",
                    "Key Detail": "Clavulanate, sulbactam, tazobactam, avibactam, and vaborbactam"
                }
            }
        }
    ]
}
