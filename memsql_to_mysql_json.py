from memsql.common import database

def get_connection(db='<source>', host='<hostname<>', port=3306, user='<user>', password='<pwd>'):
    """ Returns a new connection to the database. """
    return database.connect(
        host=host, port=port, user=user, password=password, database=db)

def consume_multi_result_set(conn, proc, args):
    """ Calls a multi-result set SP and loops through the results. """
    query = 'CALL %s(%s)' % (proc, args)
    result_set_count = 1
    for res in conn.query(query):
        print ("Processing result set %s." % result_set_count)
        for val in res.values:
            assert len(res.fieldnames) == len(val)
            print (zip(res.fieldnames, val))
        result_set_count += 1
        print ("")

def main():
    with get_connection(db="db") as conn:
        proc = 'select 1;'
        args = '1'
        consume_multi_result_set(conn, proc, args)

if __name__ == '__main__':
    main()


    def my_list_cmp(list1, list2):
        if (list1.__len__() != list2.__len__()):
            return False

        for l in list1:
            found = False
            for m in list2:
                res = my_obj_cmp(l, m)
                if (res):
                    found = True
                    break

            if (not found):
                return False

        return True


    def my_obj_cmp(obj1, obj2):
        if isinstance(obj1, list):
            if (not isinstance(obj2, list)):
                return False
            return my_list_cmp(obj1, obj2)
        elif (isinstance(obj1, dict)):
            if (not isinstance(obj2, dict)):
                return False
            exp = set(obj2.keys()) == set(obj1.keys())
            if (not exp):
                # print(obj1.keys(), obj2.keys())
                return False
            for k in obj1.keys():
                val1 = obj1.get(k)
                val2 = obj2.get(k)
                if isinstance(val1, list):
                    if (not my_list_cmp(val1, val2)):
                        return False
                elif isinstance(val1, dict):
                    if (not my_obj_cmp(val1, val2)):
                        return False
                else:
                    if val2 != val1:
                        return False
        else:
            return obj1 == obj2

        return True


    dictObj = {"foo": "bar", "john": "doe"}
    reorderedDictObj = {"john": "doe", "foo": "bar"}
    dictObj2 = {"abc": "def"}
    dictWithListsInValue = {'A': [{'X': [dictObj2, dictObj]}, {'Y': 2}], 'B': dictObj2}
    reorderedDictWithReorderedListsInValue = {'B': dictObj2, 'A': [{'Y': 2}, {'X': [reorderedDictObj, dictObj2]}]}
    a = {"L": "M", "N": dictWithListsInValue}
    b = {"L": "M", "N": reorderedDictWithReorderedListsInValue}

    print(my_obj_cmp(a, b))  # gives true
