
from gnr.web.gnrbaseclasses import BaseComponent

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        # r.fieldcell('name_competition')
        r.fieldcell('contest_director_id')
        r.fieldcell('name')
        r.fieldcell('venue')
        r.fieldcell('date')
        r.fieldcell('state_code')
        # r.fieldcell('contest_director_full_name')

    def th_options(self):
        return dict(partitioned=True)
