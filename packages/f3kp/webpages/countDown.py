class GnrCustomWebPage(object):
    py_requires = 'th/th:TableHandler'

    def main(self,root,**kwargs):
        root.data('counter','')
        root.data('countDown','')
        root.data('finish','')
        root.div ('time finish :')
        root.div('^finish')
        root.div('current time :')
        root.div('^current')

        root.button('Start Task', action='FIRE start;SET counting=true')
        root.button('Start CountDown',action='SET running=true;')
        root.div('count Down :')
        root.div('^countDown')
        root.checkBox('^running',label='Run')
        root.dataController("""
                                var finish = new Date();
                                finish.setSeconds(finish.getSeconds()+60);
                                genro.setData('finish',finish);

                                """,start='^start')

        root.dataController("""if(counting){
                                var now = new Date();
                                genro.setData('current',now);
                                }

                                """,start='^counting',counting='^counting',_timing=1)

        root.dataController("""
                                if(running){var end_task=new Date(finish);
                                            var now = new Date();
                                            var countDown= parseInt((end_task-now)/1000);
                                            if (countDown==0){
                                                            genro.setData('running',false);
                                                            genro.setData('countDown','00:00');}
                                                        
                                                        else{
                                                            var minutes= parseInt(countDown/60);
                                                            var seconds= countDown-(minutes*60);
                                                            var display= minutes+':'+seconds;
                                                            genro.setData('countDown',display);
                                                            }
                                            }
        
                            """,_timing=1,running='^running',counter='=counter',finish='=finish')

        root.script(""" 
                      function countDown(counter) {
                                        var finish = genro.getData('finish');
                                        var now= new Date();
                                        
                                        if (now<finish){
                                                        genro.setData('counter',counter-1);
                                        
                                                        var countDown=counter-1;
                                                        
                                                        if (countDown==0){
                                                            genro.setData('running',false);
                                                            genro.setData('countDown','00:00');}
                                                        
                                                        else{
                                                            var minutes= parseInt(counter/60);
                                                            var seconds= counter-(minutes*60);
                                                            var display= minutes+':'+seconds;
                                                            genro.setData('countDown',display);
                                                            }
                                                        }
                                        else {genro.setData('running',false);}

                                        }
                            """)