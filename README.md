Fixes "AttributeError: can't set attribute" bug in Seeds of Chaos v0.4.09 by replacing invalid logic in the reasearch.ryp and buildings.ryp game files. I expect devs will offically patch this at somepoint but until then this should allow you to continue research progress past this specific contract.
Patch has been tested to work with prior exsisting saves.

1. Download patched game files reasearch.rypc and buildings.rypc

2. Navigate to game folder location (you can do this from the cog wheel in steam under "Manage - Browse local files")

3. Navigate to game/core/ folder and replace the original .rypc files with the patched ones.

Enjoy!

Changelog for Nerds/Devs :)

Reasearch.rypc changes;
File "game/core/research.rpy", line 506, in on_complete{} 
  
  Original =   
          
           {castle.buildings ['brothel'].military_effectiveness += 0.1
            
            castle.buildings['brothel'].total_military_bonus += 0.1}
            
  Patched = 
  
          {brothel = castle.buildings['brothel']    
              
              if not hasattr(brothel, 'research_military_bonus'):
              
                 brothel.research_military_bonus = 0
              
              brothel.research_military_bonus += 0.1
              
              brothel.military_effectiveness += 0.1}

##Calls for new object "research_military_bouns" and applies bonus to stats

Buildings.rypc changes;
File "game/core/buildings.rpy", line 537, def_init_{}

  New line = 
  
          {self.research_military_bonus = 0}

##Inits new object "research_military_bonus" in brothel class

File "game/core/buildings.rpy", line 642, def total military_bouns{}
  
  Original = 
  
          {  _total = 0
   
                  for id in self.assets:
                  
                        asset = assets_data[id] 
                    
                    for b, e in asset.bonus:
                    
                          if b == "military":
                          
                              _total += e
                          
                          elif b == "spy efficiency":
                          
                              _total += e}

  Patched =  
  
            { _total = getattr(self, 'research_military_bonus', 0)
                 
                 for id in self.assets:
                 
                    asset = assets_data[id]
                    
                    for b, e in asset.bonus:
                    
                        if b in ("military", "spy efficiency"):
                        
                            _total += e}

##Defines total_military_bonus and calculates new visible stat
