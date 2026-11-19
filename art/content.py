"""Stories for the 18 November 2026 page. Sources and dates: research/sources-part-a.md and -part-b.md."""

KICKER = "THE DAY IN WORLD NEWS"
COUNTS = "40 STORIES · 7 REGIONS · ONE PAGE"
TITLE = "Wednesday 18 November 2026"
SUBTITLE = "Everything on this page happened, or was first reported, on Wednesday 18 November 2026."

REGIONS = [("ASIA", 8), ("EUROPE", 6), ("MIDDLE EAST", 4), ("AMERICAS", 9), ("AFRICA", 7), ("OCEANIA", 4), ("GLOBAL", 2)]

UTC = [
    ("GULF · PRE-DAWN", "Kuwait, Bahrain say Iranian drones downed"),
    ("SHENZHEN", "Xi greets Trump on the tarmac; APEC opens"),
    ("10:16 UTC", "Voyager 1 is one light-day from Earth"),
    ("BRUSSELS", "EU proposes new EUR 45bn loan for Kyiv"),
    ("CARACAS", "Hegseth announces Venezuela military pact"),
    ("NEW YORK · EVENING", "Van Gogh sells for record $190.4m"),
    ("WALL ST · CLOSE", "Dow down 1.1%, Nasdaq up 0.4% (AP)"),
]

LEADS = [
    dict(region="ASIA", kicker="ASIA · APEC SUMMIT", tag="CONFIRMED · CNBC, SCMP", art="summit",
         head="Xi greets Trump on the tarmac in Shenzhen",
         dek="A rare airport welcome as China hosts APEC; Xi opens the summit warning against trade barriers.",
         pin=(22.5, 114.1), o=dict(badge="XI MEETS TRUMP", bsize=13, caption="SHENZHEN · APEC LEADERS' WEEK", f1="CN", f2="US")),
    dict(region="MIDDLE EAST", kicker="MIDDLE EAST · IRAN", tag="CLAIM · KUWAIT, BAHRAIN", art="gulf",
         head="Kuwait and Bahrain intercept Iranian drones",
         dek="Both say they downed the drones, a day after a US strike on Iran's Qeshm island.",
         pin=(29.4, 48.0), o=dict(badge="INTERCEPTED", bsize=13, caption="THE GULF · PRE-DAWN 18 NOV",
                                  targets=[(0.3, 0.44, "KUWAIT"), (0.47, 0.7, "BAHRAIN")])),
    dict(region="GLOBAL", kicker="SPACE · NASA", tag="CONFIRMED · NASA, CNN", art="space",
         head="Voyager 1 is the first craft one light-day from Earth",
         dek="Launched in 1977, it is so far away that a radio signal now takes 24 hours each way.",
         pin=(28.5, -80.6), o=dict(badge="1 LIGHT-DAY", bsize=13, caption="10:16 UTC · DEEP SPACE")),
]

TILES = [
    dict(region="EUROPE", kicker="EUROPE · UKRAINE AID", tag="CONFIRMED · AFP", art="money",
         head="EU proposes new EUR 45bn loan for Ukraine",
         dek="Kyiv would repay only once Russia pays reparations.", pin=(50.8, 4.4),
         o=dict(amt="€45bn", f1="EU", f2="UA")),
    dict(region="MIDDLE EAST", kicker="MIDDLE EAST · GAZA", tag="CONFIRMED · BBC", art="strip",
         head="Israel launches central Gaza operation",
         dek="Its first announced push there since the Oct 2025 truce.", pin=(31.4, 34.4),
         o=dict(badge="FIRST SINCE TRUCE")),
    dict(region="EUROPE", kicker="EUROPE · UKRAINE WAR", tag="CONFIRMED · AL JAZEERA", art="drones_night",
         head="Russian strikes kill four in Odesa",
         dek="Officials say the historic centre was hit three times.", pin=(46.5, 30.7),
         o=dict(badge="4 KILLED", bcol=(190, 30, 40))),
    dict(region="AMERICAS", kicker="AMERICAS · ART", tag="CONFIRMED · AFP", art="art",
         head="Van Gogh sells for a record $190.4m",
         dek="'Blossoming Chestnut Trees' at Sotheby's, New York.", pin=(40.7, -74.0),
         o=dict(badge="$190.4m RECORD")),
    dict(region="AMERICAS", kicker="AMERICAS · DEFENCE", tag="CONFIRMED · REUTERS", art="parliament",
         head="US and Venezuela agree military pact",
         dek="Hegseth, in Caracas, announces joint training and intel sharing.", pin=(10.5, -66.9),
         o=dict(badge="HEGSETH IN CARACAS", f1="US")),
    dict(region="ASIA", kicker="ASIA · LABOUR", tag="CONFIRMED · DAILY STAR", art="protest",
         head="Dhaka wage protests close 55 factories",
         dek="Police report about 300 arrests in Savar and Ashulia.", pin=(23.9, 90.3),
         o=dict(badge="55 FACTORIES SHUT", bcol=(190, 30, 40))),
    dict(region="OCEANIA", kicker="OCEANIA · WEATHER", tag="CONFIRMED · RNZ", art="cyclone",
         head="Cyclone Xavier grows to Category 5",
         dek="Shelters open in the Cook Islands as it nears.", pin=(-21.2, -159.8),
         o=dict(badge="CATEGORY 5")),
    dict(region="AFRICA", kicker="AFRICA · CRICKET", tag="CONFIRMED · AFP", art="sport",
         head="Litton Das sets a Test world record",
         dek="Eight dismissals in an innings v South Africa.", pin=(-26.2, 28.0),
         o=dict(badge="8 DISMISSALS", ball="trophy")),
]

BRIEFS = [
    ("APEC", "Korea's Lee at Xi's dinner", "ASIA"),
    ("Kashmir", "Militant chief killed in mosque", "ASIA"),
    ("Narail", "Two BNP members killed", "ASIA"),
    ("Gopalganj", "BNP MP's clinic set on fire", "ASIA"),
    ("Dhaka", "Stun grenades at garment strike", "ASIA"),
    ("Jakarta", "Surprise rate rise to 6%", "ASIA"),
    ("Berlin", "Zelensky asks for air defences", "EUROPE"),
    ("Rivne", "Strikes cut power to 80+ towns", "EUROPE"),
    ("Krasnodar", "Kyiv says it hit 2 refineries", "EUROPE"),
    ("Kerch", "Russia shuts Crimean Bridge", "EUROPE"),
    ("Riyadh", "Saudis say Houthi missiles hit", "MIDDLE EAST"),
    ("Tehran", "Denies N. Macedonia plot claim", "MIDDLE EAST"),
    ("Alaska", "Peltola flips Senate seat (D)", "AMERICAS"),
    ("US House", "Democrats pick Jeffries, 251-11", "AMERICAS"),
    ("Bogota", "US gives Colombia a C-130", "AMERICAS"),
    ("Zapopan", "7-hour cartel gunfight, 3 dead", "AMERICAS"),
    ("Haiti", "Salvadoran troops raze gang HQ", "AMERICAS"),
    ("Wall St", "Dow -1.1%, Nasdaq +0.4% (AP)", "AMERICAS"),
    ("Amazon", "Uncontacted group pictured", "AMERICAS"),
    ("Pretoria", "Nigeria's envoy summoned", "AFRICA"),
    ("Plateau", "Night raid on village kills 8+", "AFRICA"),
    ("Abuja", "State Police Bill to Tinubu", "AFRICA"),
    ("Pretoria", "'Russia mercenaries' trial", "AFRICA"),
    ("Dakar", "Senegal into AFCON 2027", "AFRICA"),
    ("Kampala", "UNAIDS head: free Besigye", "AFRICA"),
    ("Fiji", "National drought disaster", "OCEANIA"),
    ("Canberra", "Visa cap lifted to 25,000", "OCEANIA"),
    ("Hobart", "Duckett ton in ODI decider", "OCEANIA"),
    ("Gaming", "PlayStation outage before GTA VI", "GLOBAL"),
]

MAPNOTE = "Pins = stories 1 to 11, coloured by region."
ALSO = "ALSO ON WEDNESDAY 18 NOVEMBER · 29 MORE STORIES"
DATECHECK = ("Left out, first reported before Wednesday: the US strike on Qeshm, the Knesset speaker vote, Nvidia's "
             "results (all Tue 17). Not yet news on Wednesday: the Xi-Trump-Putin talks and the ICJ Rohingya "
             "ruling (Thu 19), GTA VI's release (Thu 19), Cyclone Akvan's landfall (Fri 20).")
FOOTER_L = "Sources: AP · Reuters · AFP · BBC · CNN · CNBC · SCMP · Al Jazeera · RNZ · Daily Star · NASA"
FOOTER_R = "CLAIM = one side's account. Original drawings."
