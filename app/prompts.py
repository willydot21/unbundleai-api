def p_analyze(app_text: str):
    return [
        {
            "role": "system",
            "content": (
                "Eres un experto product strategist y analista de productos SaaS. "
                "Devuelves la salida en JSON con las claves: name, short_description, "
                "target_users, main_purposes (lista), high_level_features "
                "(lista de JSON<name, short_desc, category>), public_perception (3 bullets), "
                "notable_tech_assumptions (lista). No pongas texto adicional fuera del JSON."
            ),
        },
        {
            "role": "user",
            "content": (
                "Analiza esta app y responde en JSON. Texto de la app:\n<<<\n"
                f"{app_text}\n>>>\n"
            ),
        },
    ]


def p_extract(analyze_json: str):
    return [
        {
            "role": "system",
            "content": (
                "Eres un analista que transforma un análisis de producto en una lista "
                "de features independizables. Responde en JSON con la clave 'features' "
                "que contiene una lista de objetos con: id, name, description, category, "
                "complexity_estimate ('low|medium|high'), business_impact_estimate (1-5), "
                "can_be_unbundled (true|false), quick_mvp_idea (short text)."
            ),
        },
        {
            "role": "user",
            "content": (
                "Toma este análisis (JSON) y extrae features independientes:\n<<<\n"
                f"{analyze_json}\n>>>\n"
            ),
        },
    ]


def p_blueprint(feature_json: str):
    return [
        {
            "role": "system",
            "content": (
                "Eres un founder técnico que crea blueprints de MVP. "
                "Recibe un feature object y devuelve un blueprint JSON con: "
                "idea_name, one_line_pitch, target_user_persona, core_problem, "
                "core_feature_list (máx 5), nice_to_have_features, quick_tech_stack "
                "(frontend, backend, db, hosting), initial_pricing_model, "
                "go_to_market_ideas (3 bullets), first_3_metrics_to_track."
            ),
        },
        {
            "role": "user",
            "content": (
                "Genera el blueprint para este feature:\n<<<\n"
                f"{feature_json}\n>>>\n"
            ),
        },
    ]


def p_score(feature_json: str):
    return [
        {
            "role": "system",
            "content": (
                "Calcula un score numérico 0-100 que represente la viabilidad de "
                "convertir este feature en un producto independiente. Basalo en: "
                "dependency_on_parent (1-5), niche_size_estimate (1-5), "
                "competitive_density (1-5, invertido), technical_complexity "
                "(1-5, invertido). Explica en breve el cálculo en la clave 'explanation'. "
                "Devuelve JSON con: score, breakdown."
            ),
        },
        {
            "role": "user",
            "content": (
                "Calcula score para este feature:\n<<<\n"
                f"{feature_json}\n>>>\n"
            ),
        },
    ]
