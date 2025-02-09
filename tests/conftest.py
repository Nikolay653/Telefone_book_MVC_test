import pytest
from contextlib import nullcontext as does_not_raize


@pytest.fixture(
    params=[
        ("./data_contacts/test.json", 4, does_not_raize()),
        ("./data_contacts/tt.json", 0, pytest.raises(FileNotFoundError)),
        ("", 0, pytest.raises(IsADirectoryError)),
    ]
)
def data_test_load_from_file(request):
    return request.param


@pytest.fixture(
    params=[
        ("./data_contacts/save_test.json", does_not_raize()),
        ("", pytest.raises(FileNotFoundError)),
    ]
)
def data_save_to_file(request):
    return request.param


@pytest.fixture(
    params=[
        (
            1,
            "Максим",
            "Иванов",
            "Матвеевич",
            "+7(499)245-83-56",
            "Костоправы",
            "impiety embitter exposit",
            1,
        ),
        (
            2,
            "Дмитрий",
            "Сизов",
            "Макарович",
            "+7(499)439-62-77",
            "ООО «Петрофф-Аудит»",
            "stopgap pimple cooperate",
            1,
        ),
        (3, "", "", "", "", "", "", False),
    ]
)
def data_test_add_contact(request):
    return request.param


@pytest.fixture(
    params=[
        (
            1,
            "Максим",
            "Иванов",
            "Матвеевич",
            "+7(499)245-83-56",
            "Костоправы",
            "impiety embitter exposit",
        ),
        (
            2,
            "Дмитрий",
            "Сизов",
            "Макарович",
            "+7(499)439-62-77",
            "ООО «Петрофф-Аудит»",
            "stopgap pimple cooperate",
        ),
    ],
)
def data_test_update_delete(request):
    return request.param


@pytest.fixture(
    params=[
        (
            1,
            "Максим",
            "Иванов",
            "Матвеевич",
            "+7(499)245-83-56",
            "Костоправы",
            "impiety embitter exposit",
            1,
            does_not_raize(),
        ),
        (
            2,
            "Дмитрий",
            "Сизов",
            "Макарович",
            "+7(499)439-62-77",
            "ООО «Петрофф-Аудит»",
            "stopgap pimple cooperate",
            1,
            pytest.raises(TypeError),
        ),
    ],
)
def data_find_contact_by_name(request):
    return request.param
