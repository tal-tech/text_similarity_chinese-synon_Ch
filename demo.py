import preprocess as pre
import eval 
import json

def find_synontext(text,target):
    pre.stopwordslist("./bin/stopwords.txt")

    nn = eval.simChCheck()
    hezhi = 0.5  #相似度值的大小
    res  = []
    for value in text.values():
        result = nn.forward(value,target)
        result_dict = json.loads(result)

        # 现在可以提取 similarity 的值了
        similarity = result_dict["similarity"]
        print(similarity)
        if similarity > hezhi:
            res.append(value)
    print(res)

if __name__ == "__main__":
    text = {
        "text1" : "这句话呢，其实都是告诉你游戏规则，他就看你能不能看到他这个给你的规定了。",
        "text2" : "或者说你骂人一个游戏，它上面会有一个游戏的一个，这个攻略对不对？",
        "text3" : "确实如此，每个游戏都有其内在的规则和逻辑，只有理解并掌握了这些，我们才能更好地在游戏中取得成功。",
        "text4" : "对的，每款游戏都会有对应的攻略或者提示，通过学习和运用这些攻略，我们可以更好地享受游戏带来的乐趣，并提高我们的表现。",
    }
    target = "这段话其实是告诉你游戏规则，你要好好看，好好理解他的规定。"
    find_synontext(text,target)

