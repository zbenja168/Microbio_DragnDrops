BRICK = {
    "brick_num": 34,
    "brick_title": "Antivirals 1 of 2: Drugs to Treat Herpesvirus Infections",
    "games": [
        {
            "slug": "mechanisms_and_targets",
            "title": "How Antiherpetic Drugs Work",
            "subtitle": "Match each drug to its mechanism, main indications, and distinguishing feature",
            "categories": ["Mechanism", "Primary indications", "Distinguishing feature"],
            "data": {
                "Acyclovir": {
                    "Mechanism": "Guanosine analog incorporated into DNA, halting strand lengthening",
                    "Primary indications": "HSV-1, HSV-2, and varicella-zoster virus",
                    "Distinguishing feature": "Only drug of its class given both orally and IV"
                },
                "Ganciclovir": {
                    "Mechanism": "Guanosine analog activated by viral kinases",
                    "Primary indications": "Cytomegalovirus and acyclovir-resistant HSV",
                    "Distinguishing feature": "Initial phosphorylation depends on CMV UL97 phosphotransferase"
                },
                "Cidofovir": {
                    "Mechanism": "Imitates nucleotides to inhibit viral DNA polymerase",
                    "Primary indications": "CMV retinitis in patients with AIDS",
                    "Distinguishing feature": "Also used off-label for acyclovir-resistant HSV"
                },
                "Foscarnet": {
                    "Mechanism": "Pyrophosphate analog; noncompetitive inhibitor of viral polymerases",
                    "Primary indications": "Herpesvirus infections in immunocompromised patients",
                    "Distinguishing feature": "Works without any viral enzyme activation"
                }
            }
        },
        {
            "slug": "prodrugs_and_routes",
            "title": "Prodrugs, Routes, and Roles",
            "subtitle": "Match each agent to its key pharmacokinetic fact, route, and clinical role",
            "categories": ["Key pharmacokinetic fact", "Route", "Clinical role"],
            "data": {
                "Valacyclovir": {
                    "Key pharmacokinetic fact": "Prodrug of acyclovir with better GI absorption and bioavailability",
                    "Route": "Oral therapy for primary infection and recurrent breakouts",
                    "Clinical role": "Oral and genital herpes; chickenpox and shingles"
                },
                "Famciclovir": {
                    "Key pharmacokinetic fact": "Prodrug metabolized to its active form within the host",
                    "Route": "Taken orally with good GI absorption",
                    "Clinical role": "HSV-1, HSV-2, and varicella-zoster infections"
                },
                "Penciclovir": {
                    "Key pharmacokinetic fact": "Less effective than oral therapy, so reserved for mild cases",
                    "Route": "Topical application only",
                    "Clinical role": "Orolabial herpes exclusively"
                },
                "Valganciclovir": {
                    "Key pharmacokinetic fact": "Prodrug of ganciclovir relying on viral thymidine kinase activation",
                    "Route": "Given orally, while ganciclovir is IV",
                    "Clinical role": "CMV treatment in immunocompromised patients"
                },
                "Acyclovir": {
                    "Key pharmacokinetic fact": "The active parent compound of valacyclovir",
                    "Route": "The one class member usable orally and IV",
                    "Clinical role": "IV form reserved for the most severe herpes cases"
                }
            }
        },
        {
            "slug": "virus_to_treatment",
            "title": "Pick the Right Plan for the Virus",
            "subtitle": "Match each herpesvirus scenario to its treatment and key clinical detail",
            "categories": ["Treatment approach", "Key clinical detail"],
            "data": {
                "HSV-1 / HSV-2": {
                    "Treatment approach": "Acyclovir, valacyclovir, famciclovir, or ganciclovir",
                    "Key clinical detail": "Causes orolabial and genital herpes; lays dormant in neurons"
                },
                "Varicella-zoster virus": {
                    "Treatment approach": "Oral valacyclovir or acyclovir",
                    "Key clinical detail": "Chickenpox and shingles; chickenpox most often left untreated"
                },
                "Epstein-Barr virus": {
                    "Treatment approach": "Symptomatic care with acetaminophen and NSAIDs",
                    "Key clinical detail": "Antivirals not clinically effective for infectious mononucleosis"
                },
                "CMV in the immunocompromised": {
                    "Treatment approach": "Ganciclovir, valganciclovir, cidofovir, or foscarnet",
                    "Key clinical detail": "Treated when symptomatic or as prophylaxis in transplant recipients"
                },
                "Acyclovir-resistant HSV": {
                    "Treatment approach": "Foscarnet, since it needs no activation",
                    "Key clinical detail": "Resistance from mutations lowering viral thymidine kinase activity"
                },
                "Ganciclovir-resistant CMV": {
                    "Treatment approach": "Add foscarnet or increase the ganciclovir dose",
                    "Key clinical detail": "Resistance arises from UL97 gene mutation"
                }
            }
        },
        {
            "slug": "toxicities_and_interactions",
            "title": "Toxicities and Interactions",
            "subtitle": "Match each drug to its hallmark adverse effects and the way to manage them",
            "categories": ["Hallmark adverse effects", "Management / caution"],
            "data": {
                "Foscarnet": {
                    "Hallmark adverse effects": "Electrolyte imbalances: hypokalemia, hypocalcemia, hypomagnesemia",
                    "Management / caution": "Monitor renal function; aggressive pre-hydration with fluids"
                },
                "Acyclovir": {
                    "Hallmark adverse effects": "Increased liver enzymes, seizure risk, phlebitis when IV",
                    "Management / caution": "Proper hydration avoids crystal nephropathy from the IV form"
                },
                "Ganciclovir": {
                    "Hallmark adverse effects": "Leukopenia, thrombocytopenia, and anemia",
                    "Management / caution": "Avoid tenofovir; they compete for renal excretion, damaging kidneys"
                },
                "Antiherpetics as a class": {
                    "Hallmark adverse effects": "Potential renal impairment, since all are renally cleared",
                    "Management / caution": "Use other nephrotoxic medications cautiously or not at all"
                }
            }
        }
    ]
}
