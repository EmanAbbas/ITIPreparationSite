from haystack import indexes
from models import Question, Answer

class QuestionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    boay = indexes.CharField(model_attr='body', faceted=True)

    question = indexes.CharField()

    content_auto = indexes.EdgeNgramField(model_attr='body')

    def get_model(self):
        return Answer

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def prepare_answer(self, obj):
        return obj.question_id.header