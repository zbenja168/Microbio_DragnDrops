BRICK = {
    "brick_num": 9,
    "brick_title": "Vancomycin and Bacitracin",
    "games": [
        {
            "slug": "wall_assembly",
            "title": "Building the Bacterial Wall",
            "subtitle": "Match each cell-wall player to its identity, its job, and the drug that exploits it",
            "categories": ["What it is", "Job in wall building", "Drug connection"],
            "data": {
                "NAM": {
                    "What it is": "N-acetylmuramic acid, one glycan of peptidoglycan",
                    "Job in wall building": "Joined first to bactoprenol at the membrane surface",
                    "Drug connection": "Bacitracin blocks it from ever joining bactoprenol"
                },
                "NAG": {
                    "What it is": "N-acetyl-D-glucosamine, the other peptidoglycan glycan",
                    "Job in wall building": "Added second, onto the bactoprenol-NAM group",
                    "Drug connection": "Half of the new unit vancomycin keeps off the chain"
                },
                "Bactoprenol": {
                    "What it is": "Lipid carrier sitting in the membrane",
                    "Job in wall building": "Ferries the NAM-NAG unit across to the outer wall",
                    "Drug connection": "Bacitracin's block leaves it with no NAM to carry"
                },
                "Transpeptidase": {
                    "What it is": "Bacterial enzyme working on finished chains",
                    "Job in wall building": "Cross-links chains through peptide bridges into a rigid network",
                    "Drug connection": "Cross-linkage fails once vancomycin ties up the peptide terminus"
                },
                "D-alanyl-D-alanine terminus": {
                    "What it is": "End of the amino acid peptide on new units",
                    "Job in wall building": "Peptide tail needed for elongation and cross-linking",
                    "Drug connection": "Vancomycin's binding site, blocking peptidoglycan polymerization"
                }
            }
        },
        {
            "slug": "pick_the_drug",
            "title": "Pick the Right Drug",
            "subtitle": "Match each scenario to the drug called for, the reason, and its watch-out",
            "categories": ["Drug called for", "Why it fits", "Adverse effect to watch"],
            "data": {
                "Serious MRSA infection": {
                    "Drug called for": "IV vancomycin, a glycopeptide",
                    "Why it fits": "Very few antibiotics can cover MRSA",
                    "Adverse effect to watch": "Nephrotoxicity, its most clinically relevant toxicity"
                },
                "Superficial skin infection": {
                    "Drug called for": "Bacitracin ointment",
                    "Why it fits": "Typically used topically for superficial skin infections",
                    "Adverse effect to watch": "Contact dermatitis from topical formulations"
                },
                "Cellulitis growing MRSA plus group A strep": {
                    "Drug called for": "IV vancomycin as a single agent",
                    "Why it fits": "One drug covers both cultured organisms",
                    "Adverse effect to watch": "Red man syndrome if the infusion runs fast"
                },
                "Eye infection treated with an ophthalmic preparation": {
                    "Drug called for": "Ophthalmic-dosage bacitracin",
                    "Why it fits": "Bacitracin also comes in ophthalmic dosage forms",
                    "Adverse effect to watch": "Blurred vision"
                }
            }
        },
        {
            "slug": "vanc_toxicity_tracker",
            "title": "Vancomycin Toxicity Tracker",
            "subtitle": "Match each adverse effect to why it happens and its prevention or key fact",
            "categories": ["Why it happens", "Prevention or key fact"],
            "data": {
                "Nephrotoxicity": {
                    "Why it happens": "Drug accumulates in proximal tubular epithelial cells, inducing apoptosis",
                    "Prevention or key fact": "Common; AUC/MIC-based PK dosing reduces its occurrence"
                },
                "Ototoxicity": {
                    "Why it happens": "Vancomycin accumulates in the inner ear",
                    "Prevention or key fact": "Rare; risk rises with aminoglycosides and furosemide"
                },
                "Red man syndrome": {
                    "Why it happens": "Mast cells release histamine, causing diffuse body flushing",
                    "Prevention or key fact": "Pretreat with an antihistamine and infuse over 1-4 hours"
                },
                "Thrombophlebitis and infusion pain": {
                    "Why it happens": "Local reaction where the drug is infused",
                    "Prevention or key fact": "Far more common than kidney or ear toxicity"
                }
            }
        }
    ]
}
