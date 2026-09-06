BRICK = {
    "brick_num": 30,
    "brick_title": "Antibiotic Stewardship",
    "games": [
        {
            "slug": "resistance_mechanisms",
            "title": "How Bacteria Become Resistant",
            "subtitle": "Match each resistance mechanism to how it arises and its lecture example",
            "categories": ["How Resistance Arises", "Lecture Example"],
            "data": {
                "Intrinsic resistance": {
                    "How Resistance Arises": "Resistance is natural to the organism itself",
                    "Lecture Example": "E. coli resists vancomycin — drug too large to penetrate the cell wall"
                },
                "Selection pressure": {
                    "How Resistance Arises": "Antibiotics kill susceptible bacteria, leaving resistant strains to multiply",
                    "Lecture Example": "Oral vancomycin clears susceptible gut Enterococci, letting VRE predominate"
                },
                "Acquired resistance": {
                    "How Resistance Arises": "Resistant genes transferred between different bacterial species",
                    "Lecture Example": "DNA picked up from dead bacterial fragments in the environment"
                },
                "Enzyme inactivation": {
                    "How Resistance Arises": "Bacterial enzymes break down the antibiotic itself",
                    "Lecture Example": "Beta-lactamase destroys the beta-lactam structure of the drug"
                }
            }
        },
        {
            "slug": "enzymes_and_resistant_threats",
            "title": "Resistance Enzymes and MDR Organisms",
            "subtitle": "Match each enzyme or resistant organism to what it is and its resistance detail",
            "categories": ["What It Is", "Resistance Detail"],
            "data": {
                "Beta-lactamase": {
                    "What It Is": "Bacterial enzyme that cleaves the beta-lactam structure",
                    "Resistance Detail": "Countered by pairing clavulanate, sulbactam, or tazobactam with the drug"
                },
                "Extended-spectrum beta-lactamases (ESBLs)": {
                    "What It Is": "Beta-lactamases made by some gram-negative bacteria",
                    "Resistance Detail": "Break down all penicillins and some cephalosporins; usually treated with carbapenems"
                },
                "Carbapenem-resistant Enterobacteriaceae (CRE)": {
                    "What It Is": "Multi-drug resistant gram-negative organisms",
                    "Resistance Detail": "Enzymes break down penicillins, most cephalosporins, and carbapenems"
                },
                "Vancomycin-resistant Enterococcus (VRE)": {
                    "What It Is": "Resistant gram-positive strain of normal GI flora",
                    "Resistance Detail": "Becomes predominant after oral vancomycin eliminates susceptible Enterococci"
                },
                "RP's MDR Klebsiella pneumoniae": {
                    "What It Is": "Multidrug-resistant pneumonia pathogen from the case",
                    "Resistance Detail": "Resistant to ciprofloxacin and empiric beta-lactam, but susceptible to carbapenems"
                }
            }
        },
        {
            "slug": "asp_interventions",
            "title": "Antimicrobial Stewardship Program Interventions",
            "subtitle": "Match each ASP intervention to what the team does and its lecture detail",
            "categories": ["What The Team Does", "Lecture Detail"],
            "data": {
                "Pharmacokinetic monitoring": {
                    "What The Team Does": "Follow drug levels of select antibiotics",
                    "Lecture Detail": "Done for vancomycin and aminoglycosides"
                },
                "Clinical decision support software": {
                    "What The Team Does": "Rapidly identify pathogens with software tools",
                    "Lecture Detail": "Shortens time to starting effective treatment"
                },
                "Antibiotic restriction": {
                    "What The Team Does": "Reserve select drugs for infections with known resistant pathogens",
                    "Lecture Detail": "Ceftaroline — only fifth-generation cephalosporin, covers MRSA and VRE"
                },
                "Prospective audit and feedback": {
                    "What The Team Does": "Review prescribing of selected antibiotics",
                    "Lecture Detail": "Feedback goes directly to the prescribers"
                },
                "IV-to-oral transition": {
                    "What The Team Does": "Switch route of therapy in a timely manner",
                    "Lecture Detail": "Curbs the heavy intravenous antibiotic exposure seen in hospitals"
                }
            }
        },
        {
            "slug": "therapy_strategy",
            "title": "Choosing the Therapy Strategy",
            "subtitle": "Match each therapy approach to when it is used and its key stewardship point",
            "categories": ["When It Is Used", "Key Stewardship Point"],
            "data": {
                "Empiric therapy": {
                    "When It Is Used": "'Best guess' coverage before the organism is identified",
                    "Key Stewardship Point": "Often broad-spectrum at first, then narrowed to limit pathogen exposure"
                },
                "Targeted (definitive) therapy": {
                    "When It Is Used": "Begins once culture and sensitivity results are known",
                    "Key Stewardship Point": "Choose drugs that are safe, effective, narrow in spectrum, and cost effective"
                },
                "Narrow-spectrum antibiotics": {
                    "When It Is Used": "Preferred when the causative bacteria are known",
                    "Key Stewardship Point": "Minimize gut microbiome disruption and reduce resistance risk"
                },
                "Broad-spectrum antibiotics": {
                    "When It Is Used": "Warranted for empiric coverage of a suspected infection",
                    "Key Stewardship Point": "Kill beneficial bacteria too, driving resistance when used unnecessarily"
                }
            }
        }
    ]
}
