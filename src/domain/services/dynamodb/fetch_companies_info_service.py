import csv

from src.infra.dynamodb.dynamodb_repository import DynamoDBRepository


class FetchCompaniesInfoService:
    @staticmethod
    def fetch_companies_with_scan(
        repository: DynamoDBRepository,
        table_name: str,
        attributes_to_get: list[str],
    ) -> list[dict]:
        return repository.scan_table(
            table_name=table_name, attributes_to_get=attributes_to_get
        )

    @staticmethod
    def process_companies(companies: list[dict[str]]) -> list[list]:
        processed_data = []
        for item in companies:
            company_id = item.get("id", {}).get("S", "")
            company_name = item.get("companyName", {}).get("S", "")
            company_status = item.get("status", {}).get("S", "ACTIVE")
            skip_monitoring = item.get("skipMonitoring", {}).get("BOOL", False)

            processed_data.append(
                [company_id, company_name, company_status, skip_monitoring]
            )
        return processed_data

    @staticmethod
    def save_to_csv(data: list[list], file_path: str):
        header = ["id", "companyName", "status", "skipMonitoring"]

        with open(file_path, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)
            csv_writer.writerows(data)
        return file_path
