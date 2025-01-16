import pytest
import uuid

from src.core.category.domain.category import Category

class TesteCategory:
    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characteres(self):
        with pytest.raises(ValueError, match="name cannot be longer than 255"):
            Category("a" * 256)

    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="Filme")
        assert isinstance(category.id, uuid.UUID)

    def test_created_category_with_default_values(self):
        category = Category(name="Filme")
        assert category.name == "Filme"
        assert category.description == ""
        assert category.is_active is True
    
    def test_category_is_created_as_active_by_default(self):
        category = Category(name="Filme")
        assert category.is_active is True

    def teste_category_is_created_with_provided_values(self):
        cat_id = uuid.uuid4()
        category = Category(id=cat_id, name="Filme", description="Categoria de filmes", is_active=False)
        assert category.id == cat_id
        assert category.name == "Filme"
        assert category.description == "Categoria de filmes"
        assert category.is_active is False

    def test_category_str(self):
        category = Category(name="Filme")
        assert str(category) == "Filme -  (True)"

    def test_category_repr(self):
        category = Category(name="Filme")
        assert repr(category) == "<Category Filme ({})>".format(category.id)

    def test_cannot_create_category_with_empty_name(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            Category(name="") 

class TestUpdateCategory:
    def test_update_category_with_name_and_description(self):
        category = Category(name="Filme", description="Filmes em geral")

        category.update_category("Série", "Séries em geral")

        assert category.name == "Série"
        assert category.description == "Séries em geral"

    def test_update_category_with_invalid_name_raises_exception(self):
        category = Category(name="Filme", description="Filmes em geral")

        with pytest.raises(ValueError, match="name cannot be longer than 255"):
            category.update_category("a" * 256, "Séries em geral")
    
    def test_update_category_with_empty_name_raises_exception(self):
        category = Category(name="Filme", description="Filmes em geral")

        with pytest.raises(ValueError, match="name cannot be empty"):
            category.update_category("", "Séries em geral")

class TestActivateCategory:
    def test_activate_category(self):
        category = Category(name="Filme", description="Filmes em geral", is_active=False)

        category.activate()

        assert category.is_active is True

    def test_activate_active_category(self):
        category = Category(name="Filme", description="Filmes em geral", is_active=True)

        category.activate()

        assert category.is_active is True

class TestDeactivateCategory:
    def test_deactivate_category(self):
        category = Category(name="Filme", description="Filmes em geral", is_active=True)

        category.deactivate()

        assert category.is_active is False

    def test_deactivate_inactive_category(self):
        category = Category(name="Filme", description="Filmes em geral", is_active=False)

        category.deactivate()

        assert category.is_active is False

class TestEquality:
    def test_when_categories_have_same_id_they_are_equal(self):
        common_id = uuid.uuid4()
        category1 = Category(id=common_id, name="Filme")
        category2 = Category(id=common_id, name="Filme")

        assert category1 == category2

    def test_equality_different_classes(self):
        class Dummy:
            pass

        common_id = uuid.uuid4()
        category = Category(name="Filme", id=common_id)
        dummy = Dummy()
        dummy.id = common_id

        assert category != dummy