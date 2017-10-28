from core.renderers import ShelfJSONRenderer


class BookJSONRenderer(ShelfJSONRenderer):
    object_label = 'book'
    pagination_object_label = 'books'
    pagination_count_label = 'bookCount'
