"""Stories for the 18 November 2026 page. Sources and dates: research/sources-part-a.md and -part-b.md."""

KICKER = "THE DAY IN WORLD NEWS"
COUNTS = "47 STORIES · 7 REGIONS · ONE PAGE"
TITLE = "Wednesday 18 November 2026"
SUBTITLE = "Everything on this page happened, or was first reported, on Wednesday 18 November 2026."

REGIONS = [("ASIA", 11), ("EUROPE", 7), ("MIDDLE EAST", 5), ("AMERICAS", 11), ("AFRICA", 7), ("OCEANIA", 4), ("GLOBAL", 2)]

UTC = [
    ("GULF · PRE-DAWN", "Kuwait, Bahrain say Iranian drones downed"),
    ("07:00 UTC · LONDON", "UK inflation rises to 3.6% (ONS)"),
    ("SHENZHEN", "Xi greets Trump on the tarmac; APEC opens"),
    ("10:16 UTC", "Voyager 1 is one light-day from Earth"),
    ("BRUSSELS", "EU proposes new EUR 45bn loan for Kyiv"),
    ("19:00 UTC · FED", "Minutes: almost all see more hikes"),
    ("WALL ST · CLOSE", "Dow down 1.1%, Nasdaq up 0.4% (AP)"),
]

LEADS = [
    dict(region="ASIA", kicker="ASIA · APEC SUMMIT", tag="CONFIRMED · CNBC, SCMP", art="summit",
         head="Xi greets Trump on the tarmac in Shenzhen",
         dek="A rare airport welcome as China hosts APEC; Xi opens the summit warning against trade barriers.",
         pin=(22.5, 114.1), o=dict(badge="XI MEETS TRUMP", bsize=13, caption="SHENZHEN · APEC LEADERS' WEEK", f1="CN", f2="US", n1="XI", n2="TRUMP")),
    dict(region="MIDDLE EAST", kicker="MIDDLE EAST · IRAN", tag="CLAIM · KUWAIT, BAHRAIN", art="gulf",
         head="Kuwait and Bahrain intercept Iranian drones",
         dek="Both say they downed the drones, a day after a US strike on Iran's Qeshm island.",
         pin=(29.4, 48.0), o=dict(badge="INTERCEPTED", bsize=13, caption="THE GULF · PRE-DAWN 18 NOV",
                                  targets=[(0.3, 0.44, "KUWAIT"), (0.47, 0.7, "BAHRAIN")])),
    dict(region="GLOBAL", kicker="SPACE · NASA", tag="CONFIRMED · NASA, CNN", art="space",
         head="Voyager 1 is the first craft one light-day from Earth",
         dek="Launched in 1977, it is so far away that a radio signal now takes 24 hours each way.",
         pin=(28.5, -80.6), o=dict(badge="1 LIGHT-DAY", badge2="25.9bn km", bsize=13, caption="10:16 UTC · DEEP SPACE")),
]

TILES = [
    dict(region="EUROPE", kicker="EUROPE · UKRAINE AID", tag="CONFIRMED · AFP", art="money",
         head="EU proposes new EUR 45bn loan for Ukraine",
         dek="Repaid only once Russia pays reparations.", pin=(50.8, 4.4),
         o=dict(amt="€45bn", f1="EU", f2="UA")),
    dict(region="MIDDLE EAST", kicker="MIDDLE EAST · GAZA", tag="CONFIRMED · BBC", art="strip",
         head="Israel launches central Gaza operation",
         dek="Its first announced push since the 2025 truce.", pin=(31.4, 34.4),
         o=dict(badge="FIRST SINCE TRUCE")),
    dict(region="EUROPE", kicker="EUROPE · UKRAINE WAR", tag="CONFIRMED · AL JAZEERA", art="strike",
         head="Russian strikes kill four in Odesa",
         dek="Officials say the old centre was hit 3 times.", pin=(46.5, 30.7),
         o=dict(badge="4 KILLED", bcol=(190, 30, 40), place="ODESA OLD TOWN")),
    dict(region="AMERICAS", kicker="AMERICAS · US POLITICS", tag="CONFIRMED · AL JAZEERA", art="parliament",
         head="House Democrats pick Jeffries for Speaker",
         dek="He would be the first Black Speaker.", pin=(38.9, -77.0),
         o=dict(badge="CAUCUS VOTE", f1="US", bg=(220, 230, 245))),
    dict(region="EUROPE", kicker="EUROPE · ECONOMY", tag="CONFIRMED · ONS", art="chart_up",
         head="UK inflation rises to 3.6% in October",
         dek="Up from 3.5%; motor fuels gave the biggest push.", pin=(51.5, -0.1),
         o=dict(badge="CPI 3.6%", bcol=(190, 30, 40), cflag="UK")),
    dict(region="ASIA", kicker="ASIA · LABOUR", tag="CONFIRMED · DAILY STAR", art="protest",
         head="Dhaka wage protests close 55 factories",
         dek="Police report about 300 arrests.", pin=(23.9, 90.3),
         o=dict(badge="55 FACTORIES SHUT", bcol=(190, 30, 40), sign="TK 30,000")),
    dict(region="OCEANIA", kicker="OCEANIA · WEATHER", tag="CONFIRMED · RNZ", art="cyclone",
         head="Cyclone Xavier grows to Category 5",
         dek="Shelters open in the Cook Islands as it nears.", pin=(-21.2, -159.8),
         o=dict(badge="CATEGORY 5", land="COOK IS.")),
    dict(region="AMERICAS", kicker="AMERICAS · MARKETS", tag="CONFIRMED · FED, AP", art="bank",
         head="Fed minutes: almost all see more hikes",
         dek="A couple floated a bigger rise.", pin=(38.9, -77.0),
         o=dict(badge="HIKES LIKELY", bcol=(190, 30, 40), sign="FED")),
]

BRIEFS = [
    ("APEC", "Xi opens summit, decries trade walls", "ASIA"),
    ("APEC", "Korea's Lee at Xi's dinner", "ASIA"),
    ("Kashmir", "Militant chief killed in mosque", "ASIA"),
    ("Narail", "Two BNP members killed", "ASIA"),
    ("Gopalganj", "BNP MP's clinic set on fire", "ASIA"),
    ("Dhaka", "Stun grenades at garment strike", "ASIA"),
    ("Chandpur", "Dipu Moni's home burned", "ASIA"),
    ("N'ganj", "Ex-MP Osman's home torched", "ASIA"),
    ("Jakarta", "Surprise rate rise to 6%", "ASIA"),
    ("Berlin", "Zelensky asks for air defences", "EUROPE"),
    ("Rivne", "Strikes cut power to 80+ towns", "EUROPE"),
    ("Krasnodar", "Kyiv says it hit 2 refineries", "EUROPE"),
    ("Kerch", "Russia shuts Crimean Bridge", "EUROPE"),
    ("Riyadh", "Saudis say Houthi missiles hit", "MIDDLE EAST"),
    ("Tehran", "Denies N. Macedonia plot claim", "MIDDLE EAST"),
    ("Israel", "Reuters: Mossad chief urged US strikes", "MIDDLE EAST"),
    ("Sotheby's", "Van Gogh record: $190.4m", "AMERICAS"),
    ("Caracas", "Hegseth announces military pact", "AMERICAS"),
    ("Wall St", "Dow -1.1%, Nasdaq +0.4% (AP)", "AMERICAS"),
    ("Bogota", "US gives Colombia a C-130", "AMERICAS"),
    ("Zapopan", "7-hour cartel gunfight, 3 dead", "AMERICAS"),
    ("Haiti", "Salvadoran troops raze gang HQ", "AMERICAS"),
    ("Amazon", "Uncontacted group pictured", "AMERICAS"),
    ("Brasilia", "Police probe US donors over vote", "AMERICAS"),
    ("Argentina", "Wholesale inflation slows to 1.6%", "AMERICAS"),
    ("Johannesburg", "Litton Das Test record", "AFRICA"),
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
ALSO = "ALSO ON WEDNESDAY 18 NOVEMBER · 36 MORE STORIES"
DATECHECK = ("Left out, first reported before Wednesday: Pattinson cast as Bond (Mon 16), the US strike on Qeshm, the " +
             "Knesset speaker vote, Nvidia's results (Tue 17). Not yet news on Wednesday: the Xi-Trump-Putin talks, " +
             "the ICJ Rohingya ruling, Anthropic's first trade, GTA VI's release (Thu 19), Cyclone Akvan's landfall (Fri 20).")
FOOTER_L = "Sources: AP · Reuters · AFP · BBC · CNN · CNBC · SCMP · Al Jazeera · RNZ · Daily Star · NASA · ONS · Fed"
FOOTER_R = "Every story is dated 18 Nov by its source · CLAIM = one side's account · original drawings"
