
class GnrCustomWebPage(object):
    py_requires = 'th/th:TableHandler'

    def main(self,root,**kwargs):
        bc = root.borderContainer(datapath='main')
        pilot_id,full_name = self.db.table('f3kp.pilot'
                                    ).readColumns(columns='$id,$full_name',
                                                  where='$user_id=:uid',
                                                  uid=self.rootenv['user_id'])
        bc.data('.current_pilot_id', pilot_id)
        bc.data('.current_full_name', full_name)

        self.mainToolbar(bc.contentPane(region='top'))
        
        tab = bc.tabContainer(region='center',margin='2px',selectedPage='^.selectedPage')

        self.profilePane(tab.contentPane(title='!![en]Profile',pageName='profile'))
        self.competitionPane(tab.contentPane(title='!![en]Competition',pageName='competition'))
  

    def profilePane(self,pane):
        pane.thFormHandler(table='f3kp.pilot',
                            datapath='main.profile',
                            formResource = 'FormPilotPage',
                            startKey='^main.current_pilot_id',
                            addrow=False,delrow=False,
                            autoSave=True)      #usiamo l'autosave per poter salvare automaticamente i dati se il pilota compila i campi anagrafici
    
    def mainToolbar(self,pane):
        bar = pane.slotToolbar('2,pageTitle,*,logoutButton,2')
        bar.pageTitle.div('^.current_full_name',font_weight='bold')
        bar.logoutButton.button('Logout',action='genro.logout();')
        
    def competitionPane(self,pane):
        pane.plainTableHandler(table='f3kp.competition',
                                datapath='main.competition',
                                viewResource='ViewFromPilot',
                                condition_onStart=True)
    
    def currentCompetition(self,pane):
        pass