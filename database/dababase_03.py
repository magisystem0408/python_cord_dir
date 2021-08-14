import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# メモリ上に作成
engine =sqlalchemy.create_engine('sqlite:///:memory:')

Base =sqlalchemy.ext.declarative.declarative_base()

# テーブルの追加
# オブジェクト名は単数系
class Person(Base):
    __tablename__ ='persons'
    id =sqlalchemy.Column(sqlalchemy.Integer,primary_key=True,autoincrement =True)
    name =sqlalchemy.Column(sqlalchemy.String(14))

Base.metadata.create_all(engine)

Session =sqlalchemy.orm.sessionmaker(bind =engine)
session =Session()

# カラムの追加
p1 =Person(name='Mike')
session.add(p1)

p2 =Person(name='Nancy')
session.add(p2)

session.commit()

# 変更も可能
p4 =session.query(Person).filter_by(name='Mike').first()
p4.name ='mamushi'
session.add(p4)
session.commit()

persons =session.query(Person).all()
for person in persons:
    print(person.id, person.name)
