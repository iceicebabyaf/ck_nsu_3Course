import sys
import os
import argparse
import pandas as pd



from lab_da2.change_timeseries import (
    load_dataframe_from_file,
    create_periodic_dataframe,
    convert_to_datetime,
    extract_parts,
    display
)


def add_aggregates_by_weekday(df: pd.DataFrame) -> pd.DataFrame:
    """
    Создание признаков: среднее и std по дням недели для извлеченных признаков.

    Args:
        df (pd.DataFrame): Таблица с извлеченными признаками (из extract_parts) и столбцом 'timestamp'.

    Returns:
        pd.DataFrame: Исходная таблица с добавленными столбцами вида '{feature}_mean' и '{feature}_std'.

    Raises:
        KeyError: Если отсутствуют необходимые столбцы.
    """
    required_cols = ['timestamp', 'day', 'month', 'year', 'hour', 'quarter', 'weekday']
    for col in required_cols:
        if col not in df.columns:
            raise KeyError(f"Отсутствует обязательный столбец '{col}'.")

    agg_cols = ['day', 'month', 'year', 'hour', 'quarter']
    aggs = {col: ['mean', 'std'] for col in agg_cols}

    group = df.groupby('weekday').agg(aggs).reset_index()
    new_cols = ['weekday']
    for col in agg_cols:
        new_cols.append(f'{col}_mean')
        new_cols.append(f'{col}_std')
    group.columns = new_cols

    result = df.merge(group, on='weekday', how='left')

    return result


def example_main_synthetic():
    input_df = create_periodic_dataframe(
        start_timedate_point="2025-09-16 02:35:00",
        periods=15, freq="14h"
    )
    transformed_df = convert_to_datetime(input_df)
    extracted_df = extract_parts(transformed_df)
    extracted_df['timestamp'] = transformed_df['timestamp']
    result_df = add_aggregates_by_weekday(extracted_df)
    print(result_df)

    if not os.path.exists("output"):
        os.makedirs("output")
    result_df.to_csv('output/result_synthetic.csv', index=False)
    print("Результат сохранен в 'result_synthetic.csv'")


def main_read_file(input_csv):
    input_df = load_dataframe_from_file(input_csv)
    transformed_df = convert_to_datetime(input_df)
    extracted_df = extract_parts(transformed_df)
    extracted_df['timestamp'] = transformed_df['timestamp']
    result_df = add_aggregates_by_weekday(extracted_df)
    print(result_df)

    if not os.path.exists("output"):
        os.makedirs("output")
    output_csv = os.path.splitext(os.path.basename(input_csv))[0] + '_result.csv'
    result_df.to_csv("output/" + output_csv, index=False)
    print(f"Результат сохранен в '{output_csv}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Работа с временными метками (timeseries) с добавлением агрегатов."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--example_synthetic",
        action="store_true",
        help="Сгенерировать синтетические временные метки."
    )
    group.add_argument(
        "--file",
        type=str,
        help="Загрузить данные из CSV файла."
    )

    args = parser.parse_args()

    if args.example_synthetic:
        example_main_synthetic()
    elif args.file:
        main_read_file(args.file)