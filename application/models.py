from . import db
import sqlalchemy


# Create mappping table to link capital with some tables, and country with others..?
# Do we have some one-to-many and other many to many relationships?



class City(db.Model):
    __tablename__ = 'capitals'

    capital = db.Column(db.String(64),
                        primary_key=True)

    country_or_territory = db.Column(db.String(64),
                        index=True,
                        unique=False,
                        nullable=False)

    population = db.Column(db.Integer,
                        index=False,
                        unique=False,
                        nullable=False)


class Cost(db.Model):
    __tablename__ = 'cost_living_index'

    capital = db.Column(db.String(64),
                            db.ForeignKey('capitals.capital'),
                            primary_key=True)

    price_index = db.Column(db.Integer,
                            index=False,
                            unique=False,
                            nullable=False)

    rank = db.Column(db.String(64),
                            index=False,
                            unique=False,
                            nullable=False)

    avg_business_lunch = db.Column(db.String(64),
                            index=False,
                            unique=False,
                            nullable=False)

    avg_rent_85m2_standard = db.Column(db.String(64),
                            index=False,
                            unique=False,
                            nullable=False)

    public_trans_monthly = db.Column(db.String(64),
                            index=False,
                            unique=False,
                            nullable=False)


class Happiness(db.Model):
    __tablename__ = 'world_happiness'

    country = db.Column(db.String(64),
                        # db.ForeignKey('capitals.country_or_territory'),
                        primary_key=True)

    rank = db.Column(db.Integer,
                            index=False,
                            unique=False,
                            nullable=False)

    score = db.Column(db.Integer,
                            index=False,
                            unique=False,
                            nullable=False)

    healthy_life_expectancy = db.Column(db.Float,
                            index=False,
                            unique=False,
                            nullable=False)

    freedom_to_make_life_choices = db.Column(db.Float,
                            index=False,
                            unique=False,
                            nullable=False)

    generosity = db.Column(db.Float,
                            index=False,
                            unique=False,
                            nullable=False)

    perceptions_of_corruption = db.Column(db.Float,
                            index=False,
                            unique=False,
                            nullable=False)


class Migrant(db.Model):
    __tablename__ = 'migrant_acceptance'

    country = db.Column(db.String(64),
                        # db.ForeignKey('capitals.country_or_territory'),
                        primary_key=True)

    index = db.Column(db.Float,
                             index=False,
                             unique=False,
                             nullable=False)


class AvgWeather(db.Model):
    __tablename__ = 'average_weather_jan_july'

    capital = db.Column(db.String(64),
                        db.ForeignKey('capitals.capital'),
                        primary_key=True)

    jan_avg = db.Column(db.Integer,
                             index=False,
                             unique=False,
                             nullable=False)

    july_avg = db.Column(db.Integer,
                           index=False,
                           unique=False,
                           nullable=False)


class Sun(db.Model):
    __tablename__ = 'sunrise_sunset'

    capital = db.Column(db.String(64),
                        db.ForeignKey('capitals.capital'),
                        primary_key=True)

    latitude = db.Column(db.Float,
                            index=False,
                            unique=False,
                            nullable=False)

    longitude = db.Column(db.Float,
                            index=False,
                            unique=False,
                            nullable=False)

    shortest_day = db.Column(db.String(64),
                            index=False,
                            unique=False,
                            nullable=False)

    longest_day = db.Column(db.String(64),
                            index=False,
                            unique=False,
                            nullable=False)




#     def to_dict(self):
#        '''Return object data in easily serializable format'''
#        return {
#            'message_text' : self.message_text,
#            'message_id'   : self.message_id,
#            'user_id'      : self.user_id
#        }



#     def to_dict(self):
#        '''Return object data in easily serializable format'''
#        return {
#            'chat_id' : self.chat_id,
#            # 'users': self.message_id,
#        }