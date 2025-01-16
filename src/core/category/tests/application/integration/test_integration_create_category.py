from uuid import UUID
from src.core.category.application.create_category import CreateCategory, CreateCategoryRequest
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestIntegrationCreateCategory:
  def test_create_category_with_valid_data(self):
        repository = InMemoryCategoryRepository()
        use_case = CreateCategory(repository=repository)
        request = CreateCategoryRequest(
            name="Filme",
            description="Categoria para filmes",
            is_active=True
        )
        response = use_case.execute(request)

        assert response.id is not None
        assert isinstance(response.id, UUID)
        assert len(repository.categories) == 1
        assert repository.categories[0].id == response.id

        persisted_category = repository.categories[0]
        persisted_category.id == response.id
        persisted_category.name == request.name
        persisted_category.description == request.description
        persisted_category.is_active == request.is_active