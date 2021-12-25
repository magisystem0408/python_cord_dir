from optparse import OptionParser
from optparse import OptionGroup


def main():
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage)

    #     destは変数の入れる先
    #
    parser.add_option('-f', '--file', action='store',
                      type="string", dest='filename',
                      help="filename"
                      )
    parser.add_option("-n", "--num", action='store', type="int", dest='num')

    # ture or false関連
    parser.add_option("-v", action="store_true", dest="verbose")
    parser.add_option("-v", action="store_false", dest="verbose")

    # -rをつけるとconstのrootを使用してuser_nameとして理解される
    parser.add_option("-r", action="store_const",
                      const="root", dest="user_name")

    # コールバック関数を呼び出せる
    parser.add_option("-e", dest="env", )

    def is_release(option, opt_str, value, parser):
        if parser.values.env == "prd":
            raise parser.error("can't release")
        #     destに何か値を入れた時
        setattr(parser.values, option.dest, True)

    parser.add_option("--release", action="callback", callback=is_release, dest="release")

    group = OptionGroup(parser, "Dangerous options")
    group.add_option("-g", action="store_true", help="Group options")

    parser.add_option_group(group)

    options, args = parser.parse_args()
    print(options)
    # 入れた引数を取り出すには
    # print(options.filename)

    # 実行結果
    # test.txt

    print(args)


if __name__ == '__main__':
    main()
