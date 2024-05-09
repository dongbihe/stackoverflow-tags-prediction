from api.utils import get_bert_embeddings


def test_get_bert_embeddings():
    assert get_bert_embeddings("test").shape[0] == 1
    assert get_bert_embeddings("test").shape[1] == 768


text = "Make the current Git branch a master branch <p>I have a repository in Git. I made a branch, then did some changes both to the master and to the branch.</p>\n\n<p>Then, tens of commits later, I realized the branch is in much better state than the master, so I want the branch to \"become\" the master and disregard the changes on master.</p>\n\n<p>I cannot merge it, because I don't want to keep the changes on master. What should I do?</p>\n\n<p><em>Extra</em>: In this case, the 'old' master has already been <code>push</code>-ed to another repository such as GitHub. How does this change things?</p>\n"
expected_tags = ["git"]


# def test_predict_tags():
#    assert predict_tags(MODEL, get_bert_embeddings(text), TOP_TAGS) == expected_tags
