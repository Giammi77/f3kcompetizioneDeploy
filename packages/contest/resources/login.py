from gnr.web.gnrwebpage import BaseComponent

class LoginComponent(BaseComponent):
    def onAuthenticating_contest(self,avatar,rootenv=None):
        contest_director=self.db.table('contest.contest_director').query(where='$user_id=:user_id',
                                        user_id=avatar.user_id).fetch()
        if contest_director:
            rootenv['contest_director_id']=contest_director[0]['id']
