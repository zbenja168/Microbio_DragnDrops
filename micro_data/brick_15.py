BRICK = {
    "brick_num": 15,
    "brick_title": "DNA Gyrase and Folic Acid Inhibitors — 2 of 2: Fluoroquinolones",
    "games": [
        {
            "slug": "fq_drug_lineup",
            "title": "The Fluoroquinolone Lineup",
            "subtitle": "Match each quinolone to its grouping, clinical niche, and distinguishing fact",
            "categories": ["Grouping", "Clinical Niche or Status", "Distinguishing Fact"],
            "data": {
                "Ciprofloxacin": {
                    "Grouping": "systemic FQ, rarely used for respiratory infections",
                    "Clinical Niche or Status": "infections below the diaphragm, like pyelonephritis",
                    "Distinguishing Fact": "most effective FQ when given systemically"
                },
                "Levofloxacin": {
                    "Grouping": "respiratory fluoroquinolone with the friendliest profile",
                    "Clinical Niche or Status": "most common respiratory FQ",
                    "Distinguishing Fact": "better pseudomonas coverage and lesser side effects than moxifloxacin"
                },
                "Moxifloxacin": {
                    "Grouping": "respiratory fluoroquinolone with more side effects",
                    "Clinical Niche or Status": "respiratory infections above the diaphragm",
                    "Distinguishing Fact": "carries the greatest risk of QTc prolongation"
                },
                "Gatifloxacin": {
                    "Grouping": "respiratory fluoroquinolone by naming",
                    "Clinical Niche or Status": "only available in ophthalmic form in the US",
                    "Distinguishing Fact": "grouped with levofloxacin for S. pneumoniae coverage"
                },
                "Norfloxacin": {
                    "Grouping": "systemic FQ in the ciprofloxacin group",
                    "Clinical Niche or Status": "withdrawn from the US market, used elsewhere",
                    "Distinguishing Fact": "important FQ alongside ciprofloxacin and ofloxacin"
                },
                "Nalidixic acid": {
                    "Grouping": "an original, nonfluorinated quinolone",
                    "Clinical Niche or Status": "no longer on the market",
                    "Distinguishing Fact": "the quinolone core that FQs fluorinate"
                }
            }
        },
        {
            "slug": "gyrase_topo_mechanism",
            "title": "Gyrase, Topo IV, and the FQ Kill Switch",
            "subtitle": "Match each player in the mechanism to its identity and its action on DNA",
            "categories": ["Identity", "Action on DNA"],
            "data": {
                "DNA gyrase": {
                    "Identity": "type II topoisomerase targeted by all FQs",
                    "Action on DNA": "uniquely creates negative supercoils to prepare for replication tension"
                },
                "Topoisomerase IV": {
                    "Identity": "sister type II topoisomerase inhibited with variable specificity",
                    "Action on DNA": "relaxes negative supercoils and decatenates completed bacterial chromosomes"
                },
                "Nuclease domain": {
                    "Identity": "one of two domains in both enzymes",
                    "Action on DNA": "nicks a DNA strand so the helix can untwist and relax"
                },
                "Ligase domain": {
                    "Identity": "the domain fluoroquinolones actually inhibit",
                    "Action on DNA": "ligates, or repairs, the nick after untwisting"
                },
                "Positive supercoil": {
                    "Identity": "over-tight winding ahead of DNA-reading machinery",
                    "Action on DNA": "twists the helix tighter until it knots on itself"
                },
                "Fluoroquinolone binding": {
                    "Identity": "bactericidal blockade of the repair step",
                    "Action on DNA": "turns the enzymes into DNA shredders, halting replication"
                }
            }
        },
        {
            "slug": "fq_adverse_effects",
            "title": "FQ Adverse Effects by System",
            "subtitle": "Match each organ system to its hallmark FQ adverse effect and key detail",
            "categories": ["Hallmark Adverse Effect", "Key Detail"],
            "data": {
                "Gastrointestinal": {
                    "Hallmark Adverse Effect": "transient or mild GI upset, the most common ADR",
                    "Key Detail": "gut dysbiosis can allow C. difficile overgrowth and colitis"
                },
                "Cardiac": {
                    "Hallmark Adverse Effect": "QTc prolongation with possible torsades de pointes",
                    "Key Detail": "potassium channel inhibition; EKG monitoring is recommended"
                },
                "Neurological": {
                    "Hallmark Adverse Effect": "headache, dizziness, delirium, agitation, memory impairment",
                    "Key Detail": "rare seizures and peripheral neuropathy that can be permanent"
                },
                "Dermatological": {
                    "Hallmark Adverse Effect": "rashes in 1% to 2%, plus photosensitivity and phototoxicity",
                    "Key Detail": "after Stevens-Johnson syndrome or TEN, avoid FQs for life"
                },
                "Musculoskeletal": {
                    "Hallmark Adverse Effect": "tendinopathy and tendon rupture, most often the Achilles",
                    "Key Detail": "cartilage erosion and arthropathy in children's weight-bearing joints"
                },
                "Glucose and vessels": {
                    "Hallmark Adverse Effect": "both hyper- and hypoglycemia, plus aortic aneurysm risk",
                    "Key Detail": "hypoglycemia warning especially for elderly patients with diabetes"
                }
            }
        },
        {
            "slug": "fq_resistance_interactions",
            "title": "Resistance and Drug Interactions",
            "subtitle": "Match each interaction or resistance player to what it does and its takeaway",
            "categories": ["What It Does", "Clinical Takeaway"],
            "data": {
                "Efflux pumps": {
                    "What It Does": "actively transport the FQ back out of bacterial cells",
                    "Clinical Takeaway": "one of the two main FQ resistance mechanisms"
                },
                "Target-site mutation": {
                    "What It Does": "alters DNA gyrase or topoisomerase IV binding subunits",
                    "Clinical Takeaway": "plasmid spread can quickly protect a large bacterial population"
                },
                "MRSA and Pseudomonas aeruginosa": {
                    "What It Does": "lead the resistant gram-positive and gram-negative organisms, respectively",
                    "Clinical Takeaway": "FQ resistance is widespread across both gram stains"
                },
                "Antacid cations and supplements": {
                    "What It Does": "aluminum, magnesium, calcium, and iron chelate FQs, decreasing absorption",
                    "Clinical Takeaway": "give the FQ 4-6 hours after these products"
                },
                "Theophylline and caffeine": {
                    "What It Does": "eliminated by CYP450 1A2, which ciprofloxacin inhibits",
                    "Clinical Takeaway": "significantly decrease theophylline dose when starting ciprofloxacin"
                },
                "Beta-lactam antibiotics": {
                    "What It Does": "inhibit cell wall synthesis so FQs enter cells more easily",
                    "Clinical Takeaway": "synergistic pairing that increases FQ efficiency"
                }
            }
        }
    ]
}
