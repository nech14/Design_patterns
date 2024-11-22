curl -X GET "http://localhost:8001/api/block_period"

curl -X POST "http://localhost:8001/api/warehouse_turnover/EQUALS/2024-11-22" \
-H "Content-Type: application/json" \
-d '{
    "warehouse": {"name": "", "address": "", "unique_code": ""},
    "nomenclature": {
        "name": "",
        "group": {"name": "default_group"},
        "range": {"name": "default_range_grams"}
    }
}'


