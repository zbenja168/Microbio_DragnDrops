BRICK = {
    "brick_num": 25,
    "brick_title": "DNA Gyrase Inhibitors and Folic Acid Synthesis Inhibitors — 1 of 2: Sulfonamides",
    "games": [
        {
            "slug": "drug_profiles",
            "title": "Sulfa Drugs and Their Folate-Blocking Partners",
            "subtitle": "Match each drug to its enzyme target, key PK fact, and partner drug",
            "categories": ["Enzyme Inhibited", "Duration or Key PK Fact", "Combined With"],
            "data": {
                "Sulfadiazine": {
                    "Enzyme Inhibited": "Dihydropteroate synthase (DHPS)",
                    "Duration or Key PK Fact": "Short-acting sulfonamide, half-life about 10 hours",
                    "Combined With": "Pyrimethamine"
                },
                "Sulfamethoxazole (SMX)": {
                    "Enzyme Inhibited": "DHPS, as a competitive PABA mimic",
                    "Duration or Key PK Fact": "Intermediate-acting (9-12 h); partly metabolized by CYP2C9",
                    "Combined With": "Trimethoprim (TMP)"
                },
                "Trimethoprim (TMP)": {
                    "Enzyme Inhibited": "Dihydrofolate reductase",
                    "Duration or Key PK Fact": "Stronger affinity for bacterial than human dihydrofolate reductase",
                    "Combined With": "Sulfamethoxazole, for UTI, gut, and skin infections"
                },
                "Pyrimethamine": {
                    "Enzyme Inhibited": "Dihydrofolate reductase, like TMP",
                    "Duration or Key PK Fact": "Folate antagonist; bacteriostatic when used individually",
                    "Combined With": "Sulfadiazine, for synergistic bactericidal effect"
                }
            }
        },
        {
            "slug": "folate_pathway",
            "title": "The Bacterial Folate Pathway, Step by Step",
            "subtitle": "Match each pathway molecule to its role, its source, and its drug relevance",
            "categories": ["Role in Pathway", "How It Is Made", "Drug Relevance"],
            "data": {
                "PABA": {
                    "Role in Pathway": "Starting substrate, used with pteridine by DHPS",
                    "How It Is Made": "Taken in or produced by the bacterial cell",
                    "Drug Relevance": "Sulfonamides mimic it; overproducing it causes resistance"
                },
                "Dihydropteroic acid": {
                    "Role in Pathway": "Product of the DHPS step, converted onward to DHF",
                    "How It Is Made": "DHPS joins PABA and pteridine",
                    "Drug Relevance": "Not produced when sulfonamides block DHPS"
                },
                "Dihydrofolic acid (DHF)": {
                    "Role in Pathway": "Intermediate reduced to THF by dihydrofolate reductase",
                    "How It Is Made": "Converted from dihydropteroic acid",
                    "Drug Relevance": "Its conversion is blocked by trimethoprim and pyrimethamine"
                },
                "Tetrahydrofolic acid (THF)": {
                    "Role in Pathway": "Final cofactor for purines, thymidine, and methionine",
                    "How It Is Made": "Bacterial dihydrofolate reductase reduces DHF",
                    "Drug Relevance": "Its loss slows DNA, RNA, and protein production"
                }
            }
        },
        {
            "slug": "adverse_reactions",
            "title": "Sulfonamide Adverse Reactions",
            "subtitle": "Match each adverse reaction to its at-risk setting, cause, and prevention or response",
            "categories": ["At-Risk Setting", "Mechanism or Cause", "Prevention or Response"],
            "data": {
                "Crystalluria": {
                    "At-Risk Setting": "Any patient taking SMX/TMP tablets",
                    "Mechanism or Cause": "Drug salt precipitates in the urine",
                    "Prevention or Response": "Drink at least 8 oz of water with each tablet"
                },
                "Hyperkalemia": {
                    "At-Risk Setting": "Elderly patients and those on ACEi/ARBs or NSAIDs",
                    "Mechanism or Cause": "Potentially life-threatening rise in potassium",
                    "Prevention or Response": "Monitor patients at increased risk closely"
                },
                "Acute hemolytic anemia": {
                    "At-Risk Setting": "G6PD deficiency, identified by a positive Coombs test",
                    "Mechanism or Cause": "Sulfonamide exposure triggers rapid red cell destruction",
                    "Prevention or Response": "Recognize the rare reaction in G6PD-deficient patients"
                },
                "Kernicterus risk": {
                    "At-Risk Setting": "Last month of pregnancy",
                    "Mechanism or Cause": "Sulfonamides displace bilirubin from albumin, raising free unconjugated bilirubin",
                    "Prevention or Response": "Avoid TMP-SMX near the end of pregnancy if possible"
                },
                "Stevens-Johnson syndrome / TEN": {
                    "At-Risk Setting": "Very rare, can occur in anyone on sulfonamides",
                    "Mechanism or Cause": "Severe autoimmune skin rashes on a spectrum of body involvement",
                    "Prevention or Response": "Discontinue the drug at any new rash; can be fatal"
                },
                "Increased INR and bleeding": {
                    "At-Risk Setting": "Patients taking warfarin with SMX/TMP",
                    "Mechanism or Cause": "SMX/TMP inhibits CYP2C9, slowing warfarin metabolism",
                    "Prevention or Response": "Monitor closely for increased anticoagulation effects"
                }
            }
        },
        {
            "slug": "therapy_and_resistance",
            "title": "Single Drugs, Combos, and Bacterial Defenses",
            "subtitle": "Match each therapy approach to its effect, targets, and resistance story",
            "categories": ["Effect on Bacteria", "Enzyme Target(s)", "Resistance Angle"],
            "data": {
                "Sulfonamide alone": {
                    "Effect on Bacteria": "Bacteriostatic — stops growth without killing",
                    "Enzyme Target(s)": "Competitive inhibition of DHPS only",
                    "Resistance Angle": "Defeated by altered DHPS, efflux or decreased uptake, or extra PABA"
                },
                "TMP or pyrimethamine alone": {
                    "Effect on Bacteria": "Bacteriostatic when used individually",
                    "Enzyme Target(s)": "Dihydrofolate reductase only",
                    "Resistance Angle": "A single enzyme is relatively simple to mutate"
                },
                "SMX plus TMP combination": {
                    "Effect on Bacteria": "Synergistic, bactericidal one-two punch",
                    "Enzyme Target(s)": "Two sequential enzymes in the same folate pathway",
                    "Resistance Angle": "Mutating two crucial enzymes at once is unlikely"
                },
                "Triple sulfa preparations": {
                    "Effect on Bacteria": "No improved efficacy shown in trials",
                    "Enzyme Target(s)": "All three sulfonamides hit the same enzyme",
                    "Resistance Angle": "Stacking drugs with one shared target adds nothing"
                },
                "Selective toxicity of sulfonamides": {
                    "Effect on Bacteria": "Broad activity, since most bacteria must make their own folate",
                    "Enzyme Target(s)": "DHPS, an enzyme humans do not possess",
                    "Resistance Angle": "Folate-auxotrophic bacteria that ingest folic acid are inherently unaffected"
                }
            }
        }
    ]
}
