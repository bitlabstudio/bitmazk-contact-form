
from simple_translation.translation_pool import translation_pool

from .models import ContactFormCategory, ContactFormCategoryTranslation


translation_pool.register_translation(ContactFormCategory,
                                      ContactFormCategoryTranslation)
