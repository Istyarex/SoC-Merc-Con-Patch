init python:

    class Building(object):
        '''Base class for castle buildings'''
        def __init__(self, uid):
            self.uid = uid
            self.name = "I should not exist"
            self.available = False
            self.lvl = 0
            self.max_lvl = 0
            self.costs = []
            self.income = 0
            self.incomes = []
            self.maintenance = 0
            self.maintenances = []
            self.morale = 0
            self.morales = []
            self.research = 0
            self.researches = []
            self.capacity = 0
            self.capacities = []
            self.recruitment = 0
            self.recruitments = []
            self.thumbnail = None
            self.prereqs = []
            self.perks = []
            self.description = "Prototype class for Building, you should not see this"
            self.tooltip = ["Bug: tooltip hasn't updated"]
        
        @property
        def up_cost(self):
            '''Returns the price of new building or next upgrade'''
            if self.lvl < len(self.costs):
                return self.costs[self.lvl]
            else:
                return 0
        
        def update_tooltip(self):
            '''Called to update tooltips either after upgrade or every week.'''
            pass
        
        def build(self, ignore_max=False):
            '''Builds new upgrade level for the building'''
            if self.lvl >= self.max_lvl and ignore_max == False:
                return
            
            self.income = self.incomes[self.lvl]
            self.maintenance = self.maintenances[self.lvl]
            self.morale = self.morales[self.lvl]
            self.research = self.researches[self.lvl]
            self.capacity = self.capacities[self.lvl]
            self.recruitment = self.recruitments[self.lvl]
            
            self.lvl += 1
            
            self.update_tooltip()
        
        def weekly(self):
            '''Called each week to update state'''
            pass
        
        def can_be_built(self):
            '''Returns True if all conditions for upgrading to next level are met'''
            
            if self.lvl < self.max_lvl:
                if len(castle.scheduled_upgrades) == 0:
                    if self.costs[self.lvl] <= castle.treasury:
                        return True
            return False
        
        def can_be_shown(self):
            '''Returns True if building can be shown to player'''
            if self.lvl > 0:
                return True
            else:
                return False

    class Barracks(Building):
        '''Generic barracks but really just an orc den until maybe some gobbo troops get into the game and maybe Breeding Pit becomes a subclass because of driders'''
        def __init__(self, uid):
            super(Barracks, self).__init__(uid)
            self.name = "Orc Barracks"
            self.available = True
            self._troops = 0 
            self.equipment = 0
            self.troop_type = 'orc'
            self.costs = [100, 250, 450, 800]
            self.incomes = [0, 0, 0, 0]
            self.capacities = [30, 110, 230, 390] 
            self.retinue_capacities = [30, 40, 50, 60]
            self.morales = [0, 0, 0, 0]
            self.researches = [0, 0, 0, 0]
            self.maintenances = [0, 0, 0, 0]
            self.recruitments = [1, 2, 3, 4]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Barracks.png'
            self.prereqs = [
                ["Already Built"],
                ["Requires Technology: Ordering Chaos"],
                ["Requires Technology: Military Logistics"],
                ["Requires Technology: Tribe Negotiations"]
            ]
            
            self.perks = [[""],[""],[""],[""]]
            self.description = "A facility for housing and training orc soldiers.  Every week, any new soldiers that Andras has recruited and trained will be brought here and added to the total available soldiers. They will also be armed and armored with any available equipment from a forge, should we have one.\n Expansions and upgrades to the barracks with increase the amount of soldiers that can be kept on hand for any missions or conquests they are needed for. However, the more soldiers we have at once the more we will have to pay and the more difficult it will be to keep morale up. Other infrastructure will be needed to handle the needs of the soldiers."
            self.tooltip = []
            self.lvl = 0
            self.max_lvl = 1
            self.build()
            
            self.reserve = 0
        
        @property
        def retinue(self):
            if self.lvl == 0:
                return 0
            return self.retinue_capacities[self.lvl - 1]
        
        def reserve_equipments(self):
            value = self.equipment - self.troops
            
            if value > 0:
                return value
            return 0
        
        def weekly(self):
            
            self.perks = [ 
                [
                "Orc soldier capacity "+str(self.capacities[0]), 
                "Personal retinue "+str(self.retinue_capacities[0]), 
                "Weekly recruitment "+str(self.recruitments[0]), 
                "Military strength once filled "+str(all_troops[self.troop_type]['strength']*self.capacities[0]), 
                "Once filled, weekly maintenance "+str(all_troops[self.troop_type]['maintenance']*self.capacities[0]), 
                "Once filled, weekly morale "+str(all_troops[self.troop_type]['morale_cost']*self.capacities[0]*-1)
                ],
                
                [
                "Orc soldier capacity "+str(self.capacities[0])+"->"+str(self.capacities[1]), 
                "Personal retinue "+str(self.retinue_capacities[0])+"->"+str(self.retinue_capacities[1]), 
                "Weekly recruitment "+str(self.recruitments[0])+"->"+str(self.recruitments[1]), 
                "Military strength once filled "+str(all_troops[self.troop_type]['strength']*self.capacities[0])+"->"+str(all_troops[self.troop_type]['strength']*self.capacities[1]), 
                "Once filled, weekly maintenance "+str(all_troops[self.troop_type]['maintenance']*self.capacities[0])+"->"+str(all_troops[self.troop_type]['maintenance']*self.capacities[1]), 
                "Once filled, weekly morale "+str(all_troops[self.troop_type]['morale_cost']*self.capacities[0]*-1)+"->"+str(all_troops[self.troop_type]['morale_cost']*self.capacities[1]*-1)
                ],
                
                [
                "Orc soldier capacity "+str(self.capacities[1])+"->"+str(self.capacities[2]), 
                "Personal retinue "+str(self.retinue_capacities[1])+"->"+str(self.retinue_capacities[2]), 
                "Weekly recruitment "+str(self.recruitments[1])+"->"+str(self.recruitments[2]), 
                "Military strength once filled "+str(all_troops[self.troop_type]['strength']*self.capacities[1])+"->"+str(all_troops[self.troop_type]['strength']*self.capacities[2]), 
                "Once filled, weekly maintenance "+str(all_troops[self.troop_type]['maintenance']*self.capacities[1])+"->"+str(all_troops[self.troop_type]['maintenance']*self.capacities[2]), 
                "Once filled, weekly morale "+str(all_troops[self.troop_type]['morale_cost']*self.capacities[1]*-1)+"->"+str(all_troops[self.troop_type]['morale_cost']*self.capacities[2]*-1)
                ],
                [
                "Orc soldier capacity "+str(self.capacities[2])+"->"+str(self.capacities[3]), 
                "Personal retinue "+str(self.retinue_capacities[2])+"->"+str(self.retinue_capacities[3]), 
                "Weekly recruitment "+str(self.recruitments[2])+"->"+str(self.recruitments[3]), 
                "Military strength once filled "+str(all_troops[self.troop_type]['strength']*self.capacities[2])+"->"+str(all_troops[self.troop_type]['strength']*self.capacities[3]), 
                "Once filled, weekly maintenance "+str(all_troops[self.troop_type]['maintenance']*self.capacities[2])+"->"+str(all_troops[self.troop_type]['maintenance']*self.capacities[3]), 
                "Once filled, weekly morale "+str(all_troops[self.troop_type]['morale_cost']*self.capacities[2]*-1)+"->"+str(all_troops[self.troop_type]['morale_cost']*self.capacities[3]*-1)
                ]
            ]
            
            if self.troops < self.retinue:
                self.troops += self.recruitment + castle.recruitment_bonuses.get(self.uid, 0)
                
                if self.troops > self.retinue:
                    extra = self.troops - self.retinue
                    self.troops = self.retinue
                    self.reserve += extra
                
                elif self.troops < self.retinue:
                    extras = min(self.reserve, self.retinue - self.troops) 
                    self.troops += extras
                    self.reserve -= extras
            
            elif self.reserve < (self.capacity - self.retinue):
                self.reserve += self.recruitment + castle.recruitment_bonuses.get(self.uid, 0)
            
            if self.reserve > (self.capacity - self.retinue):
                self.reserve = (self.capacity - self.retinue)
            
            self.update_tooltip()
        
        def update_tooltip(self):
            
            equipment_value = min(self.equipment, self.troops)
            self.tooltip = [
                "Check reports on soldiers.",
                "Retinue: {:g}/{:g}".format(int(self.troops), int(self.retinue)),  
                "Equipped: {:g}/{:g}".format(int(equipment_value), int(self.troops))
            ]
        
        @property
        def troops(self):
            return self._troops
        
        @troops.setter
        def troops(self, val):
            self._troops = min(val, self.retinue)
            self._troops = max(self._troops, 0)

    class DarkSanctum(Barracks):
        '''A place where the troops need to be seperated with a fire hose'''        
        def __init__(self, uid):
            super(DarkSanctum, self).__init__(uid)
            self.name = "Dark sanctum"
            self.available = True
            self.costs = [150, 300, 600]
            self.incomes = [0, 0, 0]
            self.maintenances = [0, 0, 0]
            self.morales = [0, 0, 0]
            self.researches = [0, 0, 0]
            self.capacity = 0
            self.capacities = [10, 45, 90]
            self.retinue_capacities = [5, 10, 15]
            self.recruitments = [1, 1, 1]
            self.troop_type = 'cubi'
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Sanctum.png'
            self.prereqs = [
                ["No prerequisites for Level 1"],
                ["Requires technology: Opulence"],
                ["Requires technology: Dark Dynasty"]
            ]
            
            self.perks = [[""],[""],[""]]
            
            self.description = "Constructed underground in the tunnels, the dark sanctum is a facility to house and support the needs of magically inclined incubi and succubi. These lesser demons may live their lives focused on sex, but many of them are natural users of chaos magic and we would be remiss in not putting those skills to use. They work fantastically alongside orcs, improving the morale of the troops as well as their effectiveness in combat. Additionally, Cliohna will be able to work with them to augment our research abilities slightly.\n Jezera has her eyes on a particular succubus to head this division of the castle's forces. Apparently this powerful demon has a reputation as a romance fetishest and possesses both sexes."
            self.lvl = 0
            self.max_lvl = 1
            
            self.reserve = 0
        
        @property
        def retinue(self):
            if self.lvl == 0:
                return 0
            
            return self.retinue_capacities[self.lvl-1]
        
        def weekly(self):
            
            self.perks = [
                [
                "Incubus and Succubus capacity "+str(self.capacities[0]), 
                "Weekly recruitment "+str(self.recruitments[0]), 
                "Military strength once filled "+str(all_troops[self.troop_type]['strength']*self.capacities[0]), 
                "Once filled, weekly maintenance "+str(all_troops[self.troop_type]['maintenance']*self.capacities[0]), 
                "Once filled, weekly morale "+str(all_troops[self.troop_type]['morale_cost']*self.capacities[0]*-1), 
                "Once filled, weekly research "+str(all_troops[self.troop_type]['research']*self.capacities[0])+" RP",
                "Once filled, multiplier to orc soldier military strength +"+str(self.capacities[0]*5)+"%" 
                ],
                
                [
                "Incubus and Succubus capacity "+str(self.capacities[0])+"->"+str(self.capacities[1]), 
                "Weekly recruitment "+str(self.recruitments[0])+"->"+str(self.recruitments[1]), 
                "Military strength once filled "+str(all_troops[self.troop_type]['strength']*self.capacities[0])+"->"+str(all_troops[self.troop_type]['strength']*self.capacities[1]), 
                "Once filled, weekly maintenance "+str(all_troops[self.troop_type]['maintenance']*self.capacities[0])+"->"+str(all_troops[self.troop_type]['maintenance']*self.capacities[1]), 
                "Once filled, weekly morale "+str(all_troops[self.troop_type]['morale_cost']*self.capacities[0]*-1)+"->"+str(all_troops[self.troop_type]['morale_cost']*self.capacities[1]*-1), 
                "Once filled, weekly research "+str(all_troops[self.troop_type]['research']*self.capacities[0])+" RP ->"+str(all_troops[self.troop_type]['research']*self.capacities[1])+" RP",
                "Once filled, multiplier to orc soldier military strength +"+str(self.capacities[0]*5)+"% ->+"+str(self.capacities[1]*5)+"%"
                ],
                [
                "Incubus and Succubus capacity "+str(self.capacities[1])+"->"+str(self.capacities[2]), 
                "Weekly recruitment "+str(self.recruitments[1])+"->"+str(self.recruitments[2]), 
                "Military strength once filled "+str(all_troops[self.troop_type]['strength']*self.capacities[1])+"->"+str(all_troops[self.troop_type]['strength']*self.capacities[2]), 
                "Once filled, weekly maintenance "+str(all_troops[self.troop_type]['maintenance']*self.capacities[1])+"->"+str(all_troops[self.troop_type]['maintenance']*self.capacities[2]), 
                "Once filled, weekly morale "+str(all_troops[self.troop_type]['morale_cost']*self.capacities[1]*-1)+"->"+str(all_troops[self.troop_type]['morale_cost']*self.capacities[2])*-1, 
                "Once filled, weekly research "+str(all_troops[self.troop_type]['research']*self.capacities[1])+" RP ->"+str(all_troops[self.troop_type]['research']*self.capacities[2])+" RP",
                "Once filled, multiplier to orc soldier military strength +"+str(self.capacities[1]*5)+"% ->+"+str(self.capacities[2]*5)+"%"
                ]
            ]
            
            if self.lvl == 0:
                return
            
            castle.morale += self.morale
            castle.treasury -= self.maintenance
            
            if self.troops < self.retinue:
                
                self.troops += self.recruitment + castle.recruitment_bonuses.get(self.uid, 0)
            
            
            if self.troops > self.retinue:
                extra = self.troops - self.retinue
                self.troops = self.retinue
                self.reserve += max(0, extra)  
            
            
            elif self.troops < self.retinue:
                extras = min(self.reserve, self.retinue - self.troops)  
                self.troops += extras
                self.reserve -= extras
            
            
            if self.reserve < (self.capacity - self.retinue):
                self.reserve += self.recruitment + castle.recruitment_bonuses.get(self.uid, 0)
            
            
            self.reserve = min(self.reserve, (self.capacity - self.retinue))
            
            self.update_tooltip()
        
        def update_tooltip(self):
            
            self.tooltip = ["Check reports on sorcerors.",f"Retinue: {self.troops}/{self.retinue}"]

    class Forge(Building):
        '''Converts some iron to equipment'''
        def __init__(self, uid):
            super(Forge, self).__init__(uid)
            self.name = "Forge"
            self.available = True
            self.costs = [150, 300, 600]
            self.incomes = [30, 60, 90]
            self.maintenances = [10, 15, 20]
            self.researches = [0, 0, 0]
            self.capacities = [4, 8, 12]
            self.morales = [0, 0, 0]
            self.recruitments = [0, 0, 0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Forge.png'
            self.prereqs = [
                ["Immediately available at Level 1"],
                ["Requires Technology: Tools and Schematics"],
                ["Requires Technology: Grand Projects"]
            ]
            self.perks = [
                [
                "Max iron turned into equipment per week "+str(self.capacities[0]),
                "Equipped orc soldier increased military capacity +"+str(all_troops['orc']['equip_strength']),
                "Weekly maintenance cost "+str(self.maintenances[0])
                ],
                [
                "Max iron turned into equipment per week "+str(self.capacities[0])+"->"+str(self.capacities[1]),
                "Equipped orc soldier increased military capacity +"+str(all_troops['orc']['equip_strength']),
                "Weekly maintenance cost "+str(self.maintenances[0])+"->"+str(self.maintenances[1])
                ],
                [
                "Max iron turned into equipment per week "+str(self.capacities[1])+"->"+str(self.capacities[2]),
                "Equipped orc soldier increased military capacity +"+str(all_troops['orc']['equip_strength']),
                "Weekly maintenance cost "+str(self.maintenances[1])+"->"+str(self.maintenances[2])
                ]
            ]
            self.description = "Rosaria is the biggest producer of iron in all the Six Realms. Mines are scattered all over the realm, and can be occupied by Bloodmeen to produce iron for us. However without a forge, this metal does us no good except to be sold for a small increase in funds. Building a forge will convert that iron into usable equipment for our soldiers, dramatically increasing their capability in battle./n The forge will be built in the tunnels under Bloodmeen, near the orc barracks facilities. A forge used to be in this area, so ventilation shafts are already in place for the smoke and to supply the bellows./n Andras has a suitable forgemaster picked out, an elder minotaur from the Dragon's Tail that taught him how to smith in his youth."
            self.lvl = 0
            self.max_lvl = 1
            self.mode = "military"
            self.converted_this_week = 0
        
        def weekly(self):
            if self.lvl == 0:
                return
            
            self.converted_this_week = 0
            current_capacity = self.capacity
            if "hq_forge_tools" in avatar.ploy:
                current_capacity += 2
            
            if hasattr(all_actors["alexia"], "job_state") and all_actors["alexia"].job_state.job == "forge":
                current_capacity += 2
            
            if self.mode == "military":
                castle._iron -= current_capacity
                if castle._iron < 0:
                    castle._equipment += current_capacity + castle._iron
                    self.converted_this_week += current_capacity + castle._iron
                    castle._iron = 0
                else:
                    castle._equipment += current_capacity
                    self.converted_this_week = current_capacity
            
            elif self.mode == "balanced":
                castle._iron -= self.capacity
                if castle._iron < 0:
                    castle._morale += (self.capacity + castle._iron) * 0.25
                    self.converted_this_week = (self.capacity + castle._iron)
                    castle._iron = 0
                else:
                    castle._morale += self.capacity * 0.25
                    self.converted_this_week = self.capacity
            
            elif self.mode == "commercial":
                castle._iron -= self.capacity
                if castle._iron < 0:
                    castle.treasury += (self.capacity + castle._iron) * 4
                    self.converted_this_week = (self.capacity + castle._iron)
                    castle._iron = 0
                else:
                    castle.treasury += self.capacity * 4
                    self.converted_this_week = self.capacity
            
            self.update_tooltip()
        
        def update_tooltip(self):
            
            self.tooltip = ["Set forge mode.", f"Last week's mode: {self.mode}", f"Iron processed this week: {self.converted_this_week}"]

    class Dungeon(Building):
        '''Dungeon (contains prisoners)'''
        def __init__(self, uid):
            super(Dungeon, self).__init__(uid)
            self.name = "Dungeon"
            self.available = True
            self._prisoners = 0
            self.costs = [0, 0, 0]
            self.capacities = [100, 100, 100]
            self.maintenances = [0, 0, 0]
            self.incomes = [0, 0, 0]
            self.morales = [0, 0, 0]
            self.researches = [0, 0, 0]
            self.recruitments = [0, 0, 0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_CastleDungeon.png'
            self.prereqs = [["Already built and not expandable"],[""],[""]]
            self.perks = [["Capacity for "+str(self.capacities[0])+" prisoners"],[""],[""]]
            self.description = "A section of the underground dedicated to holding prisoners. These are generally acquired after towns or fortresses have been sacked and can later be, employed, in other roles based on what structures we have completed in the castle. However, selling slaves will always be available should some quick money be needed.\n Upgrades here will increase the amount of prisoners that can be kept at once, but there is no such option at the moment"
            
            
            
            self.prisoners_status = {
                'slave': [0, 10],
                'ransom': [0, 3],
                'gladiator': [0, 3],
                'test': [0, 5]}
            
            self.prisoners_auto = {
                'slave': False,
                'ransom': False,
                'gladiator': False,
                'test': False}
            self.lvl = 0
            self.max_lvl = 1
            self.build()
        
        def weekly(self):
            
            while self.prisoners > 0:
                if castle.morale < 20 and (self.prisoners_status['gladiator'][0] < self.prisoners_status['gladiator'][1]) and self.prisoners_auto['gladiator']:
                    castle.morale += 3
                    self.prisoners -= 1
                    self.prisoners_status['gladiator'][0] += 1
                elif (self.prisoners_status['ransom'][0] < self.prisoners_status['ransom'][1]) and self.prisoners_auto['ransom']:
                    castle.treasury += 10
                    self.prisoners -= 1
                    self.prisoners_status['ransom'][0] += 1
                elif castle.morale >= 20 and castle.morale < 60 and (self.prisoners_status['gladiator'][0] < self.prisoners_status['gladiator'][1]) and self.prisoners_auto['gladiator']:
                    castle.morale += 3
                    self.prisoners -= 1
                    self.prisoners_status['gladiator'][0] += 1
                elif (self.prisoners_status['test'][0] < self.prisoners_status['test'][1]) and self.prisoners_auto['test']:
                    castle.rp += 2
                    self.prisoners -= 1
                    self.prisoners_status['test'][0] += 1
                elif (self.prisoners_status['slave'][0] < self.prisoners_status['slave'][1]) and self.prisoners_auto['slave']:
                    castle.treasury += 5
                    self.prisoners -= 1
                    self.prisoners_status['slave'][0] += 1
                elif (self.prisoners_status['gladiator'][0] < self.prisoners_status['gladiator'][1]) and self.prisoners_auto['gladiator']:
                    castle.morale += 3
                    self.prisoners -= 1
                    self.prisoners_status['gladiator'][0] += 1
                else:
                    
                    break
            
            self.prisoners_status['slave'][0] = 0
            self.prisoners_status['ransom'][0] = 0
            self.prisoners_status['gladiator'][0] = 0
            self.prisoners_status['test'][0] = 0
            
            self.update_tooltip()
        
        def update_tooltip(self):
            
            self.tooltip = ["Decide what to do with any prisoners.", f"Prisoners available: {self.prisoners}/{self.capacity}"]
        
        
            
        @property
        def prisoners(self):
            return self._prisoners
        
        @prisoners.setter
        def prisoners(self, val):
            self._prisoners = min(val, self.capacity)
            self._prisoners = max(self._prisoners, 0)

    class Brothel(Building):
        '''Brothel (contains spies)'''
        def __init__(self, uid):
            super(Brothel, self).__init__(uid)
            self.name = "Brothel"
            self.available = True
            self.costs = [200, 300, 400]
            self.incomes = [0, 0, 0]
            self.maintenances = [5, 6, 7]
            self.morales = [0.5, 1, 1.5]
            self.capacities = [4, 6, 8]
            self.researches = [0.5, 0.75, 1]
            self.recruitments = [0, 0, 0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Brothel.png'
            self.prereqs = [
                ["Requires Technology: Fiendish Diplomacy"],
                ["Requires Technology: Silks and Smiles"],
                ["Requires Technology: The Value of Gossip"]
            ]
            self.perks = [
                [
                "Weekly maintenance "+str(self.maintenances[0]), 
                "Spy capacity "+str(self.capacities[0]), 
                "Weekly morale "+str(self.morales[0]), 
                "Weekly research "+str(self.researches[0])+" RP"
                ],
                [
                "Weekly maintenance "+str(self.maintenances[0])+"->"+str(self.maintenances[1]), 
                "Spy capacity "+str(self.capacities[0])+"->"+str(self.capacities[1]), 
                "Weekly morale "+str(self.morales[0])+"->"+str(self.morales[1]), 
                "Weekly research "+str(self.researches[0])+" RP ->"+str(self.researches[1])+" RP"
                ],
                [
                "Weekly maintenance "+str(self.maintenances[1])+"->"+str(self.maintenances[2]), 
                "Spy capacity "+str(self.capacities[1])+"->"+str(self.capacities[2]), 
                "Weekly morale "+str(self.morales[1])+"->"+str(self.morales[2]), 
                "Weekly research "+str(self.researches[1])+" RP ->"+str(self.researches[2])+" RP"
                ]
            ]
            self.description = "While they are among the weakest of the demon hordes, succubi and incubi have numerous talents that make them a near constant presence wherever the forces of chaos are at work.  Among the greatest of their members are those well versed in subterfuge and intrigue.  Fielding a team of cubi spies would be ideal for spying, infiltration, and even underhanded diplomacy./n Unfortunately, these same talented individuals have an inevitable obsession with appearances and ambiance.  Therefore, a facility that will serve as their base will need to meet those vanity needs.  Jezera has taken a keen interest in 'decorating,' and has even offered to cover a great deal of those costs out of her own pocket.  One benefit of all this expense is that it gives a place for our spies to bring targets to and interrogate them without giving anything about the castle away./n Jezera has said her girlfriend from Qerazel will be taking over operation of the castle's spies once the brothel is finished."
            self.lvl = 0
            self.max_lvl = 0
            self.mode = "military"
            self.assets = []
            
            self.military_effectiveness = 1.0
            self.blackmail_effectiveness = 1.0
            self.kidnapping_effectiveness = 1.0
            
            self.research_military_bonus = 0
            
            self.extra_capacity = 0
            self.spy_on_mission = 0
            self.spies_on_mission_detail = []
            
            self.converted_this_week = 0
        
        def next_week(self, kind):
            if kind == "military":
                return (0.15 * self.available_spies * self.military_effectiveness)
            
            elif kind == "blackmail":
                return (5.00 * self.available_spies * self.blackmail_effectiveness)
            
            elif kind == "kidnapping":
                return (-5 * self.available_spies, 0.5 * self.available_spies * self.kidnapping_effectiveness)
        
        def weekly(self):
            if "criminal_connections" in avatar.ploy:
                boost = 1.25
            else:
                boost = 1.0
            
            if self.mode == "military":
                value = 0.15 * self.available_spies * self.military_effectiveness * boost * (1 + self.total_military_bonus * 0.01)
                castle.war_readiness += value
                self.converted_this_week = value
            
            elif self.mode == "blackmail":
                value = 5 * self.available_spies * self.blackmail_effectiveness * boost * (1 + self.total_blackmail_bonus * 0.01)
                castle.treasury += value
                self.converted_this_week = value
            
            elif self.mode == "kidnapping":
                castle.treasury -= 5 * self.available_spies
                
                value = 0.5 * self.available_spies * self.kidnapping_effectiveness * boost * (1 + self.total_kidnappping_bonus * 0.01)
                castle.buildings['dungeon'].prisoners_status["slave"][0] += value
                self.converted_this_week = value
            
            self.check_if_spies_return()
            self.update_tooltip()
        
        def update_tooltip(self):
            
            self.tooltip = ["Check spy tasks.", f"Last week's mode: {self.mode}", f"Available spies: {self.available_spies}/{self.capacity}"]
        
        def check_if_spies_return(self):
            for w, n, v in self.spies_on_mission_detail:
                if w == store.week:
                    self.spy_on_mission -= n
                    if v:
                        setattr(store, v, True)
            
            self.spies_on_mission_detail = [[w, n, v] for w, n, v in self.spies_on_mission_detail if w > store.week]
        
        def send_spies(self, number, for_weeks=2, var=""):
            self.spies_on_mission_detail.append([store.week + for_weeks, number, var])
            self.spy_on_mission += number
        
        def build(self, ignore_max=False):
            super(Brothel, self).build(ignore_max)
            self.weekly()
        
        def add_asset(self, asset_id):
            self.assets.append(asset_id)
            
            asset = assets_data[asset_id]
            for b, e in asset.bonus:
                if b == "military":
                    self.military_effectiveness += (e / 100)
                elif b == "kidnapping":
                    self.kidnapping_effectiveness += (e / 100)
                elif b == "blackmail":
                    self.blackmail_effectiveness += (e / 100)
                elif b == "spy":
                    self.extra_capacity += e
        
        def has_asset(self, asset_id):
            return asset_id in self.assets
        
        def remove_asset(self, asset_id):
            self.assets.remove(asset_id)
            
            asset = assets_data[asset_id]
            for b, e in asset.bonus:
                if b == "military":
                    self.military_effectiveness -= (e / 100)
                elif b == "kidnapping":
                    self.kidnapping_effectiveness -= (e / 100)
                elif b == "blackmail":
                    self.blackmail_effectiveness -= (e / 100)
                elif b == "spy":
                    self.extra_capacity -= e
        
        @property
        def available_spies(self):
            return self.capacity + self.extra_capacity - self.spy_on_mission
        
        @property
        def total_spies(self):
            return self.capacity + self.extra_capacity
        
        @property
        def total_military_bonus(self):
            _total = getattr(self, 'research_military_bonus', 0)
            for id in self.assets:
                asset = assets_data[id]
                for b, e in asset.bonus:
                    if b in ("military", "spy efficiency"):
                        _total += e
                    
            return _total
        
        @property
        def total_kidnappping_bonus(self):
            _total = 0
            for id in self.assets:
                asset = assets_data[id]
                
                for b, e in asset.bonus:
                    if b == "kidnapping":
                        _total += e
                    elif b == "spy efficiency":
                        _total += e
            
            return _total
        
        @property
        def total_blackmail_bonus(self):
            _total = 0
            for id in self.assets:
                asset = assets_data[id]
                
                for b, e in asset.bonus:
                    if b == "blackmail":
                        _total += e
                    elif b == "spy efficiency":
                        _total += e
            
            return _total
        
        @property
        def spies(self):
            self.capacity + self.extra_capacity

    class BreedingPit(Building):
        '''Breeding pit (contains various monsters)'''
        def __init__(self, uid):
            super(BreedingPit, self).__init__(uid)
            self.name = "Breeding pit"
            self.available = True
            self.costs = [200, 300, 600]
            self.maintenances = [0, 0, 0]
            self.researches = [0, 0, 0]
            self.capacities = [6, 32, 75]
            self.retinue_capacities = [3, 8, 15]
            self.incomes = [0, 0, 0]
            self.morales = [0, 0, 0]
            self.recruitments = [0, 0, 0]
            self.troop_type = 'drider'
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_BreedingPit.png'
            self.prereqs = [
                ["Requires Technology: Monster Taming"],
                ["Requires Technology: Drider Training"],
                ["Requires Technology: Drider Naturalisation"]
            ]
            
            self.perks = [[""],[""],[""]]
            
            self.description = "One of the most terrifying things that Karnas brought down on the Six Realms were tamed, or at least semi-controlled, monsters.  The twisted creatures that wander the lands, whom generally either kept to themselves or were checked by Solancia's faithful, came down as a unified force destroyed morale better than any force of orcs could ever hope./n Caring for and housing these creatures requires very specialized facilities.  Before we even consider running breeding operations, we must first build a facility that meets these needs.  The benefits gained depends largely on the creature in question, which is in turn determined by availability of eggs and young to raise and tame.  Again, we cannot even consider taking these until we've built the basic pit facility./n The dark elves are well known for their care for monsters and would make a suitable master breeder. This is often a role often taken on by the men."
            self._driders = 0
            self.drider_recruitment = 0
            self.lvl = 0
            self.max_lvl = 0
            
            self.reserve = 0
        
        @property
        def retinue(self):
            if self.lvl == 0:
                return 0
            
            return self.retinue_capacities[self.lvl-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        @property
        def maintenance_discount(self):
            for ac in all_actors.values():
                if hasattr(ac, 'job_state'):
                    if ac.job_state.job == 'breeding':
                        return int(10 * all_actors[ac.uid].job_state.efficiency())
            return 0
        
        @property
        def free_space(self):
            
            return self.capacity - self.monsters
        
        @property
        def driders(self):
            
            return int(self._driders)
        
        @property
        def monsters(self):
            '''Returns total number of "whole" monsters, disregarding their size'''
            
            return self.driders
        
        def weekly(self):
            
            self.perks = [
                [
                "Drider capacity "+str(self.capacities[0]),
                "Personal retinue capacity "+str(self.retinue_capacities[0]),
                "Weekly recruitment "+str(self.recruitments[0]),
                "Military strength once filled "+str(all_troops[self.troop_type]['strength']*self.capacities[0]),
                "Once filled, weekly maintenance "+str(all_troops[self.troop_type]['maintenance']*self.capacities[0])
                ],
                [
                "Drider capacity "+str(self.capacities[0])+"->"+str(self.capacities[1]),
                "Personal retinue capacity "+str(self.retinue_capacities[0])+"->"+str(self.retinue_capacities[1]),
                "Weekly recruitment "+str(self.recruitments[0])+"->"+str(self.recruitments[1]),
                "Military strength once filled "+str(all_troops[self.troop_type]['strength']*self.capacities[0])+"->"+str(all_troops[self.troop_type]['strength']*self.capacities[1]),
                "Once filled, weekly maintenance "+str(all_troops[self.troop_type]['maintenance']*self.capacities[0])+"->"+str(all_troops[self.troop_type]['maintenance']*self.capacities[1])
                ],
                [
                "Drider capacity "+str(self.capacities[1])+"->"+str(self.capacities[2]),
                "Personal retinue capacity "+str(self.retinue_capacities[1])+"->"+str(self.retinue_capacities[2]),
                "Weekly recruitment "+str(self.recruitments[1])+"->"+str(self.recruitments[2]),
                "Military strength once filled "+str(all_troops[self.troop_type]['strength']*self.capacities[1])+"->"+str(all_troops[self.troop_type]['strength']*self.capacities[2]),
                "Once filled, weekly maintenance "+str(all_troops[self.troop_type]['maintenance']*self.capacities[1])+"->"+str(all_troops[self.troop_type]['maintenance']*self.capacities[2])
                ]
            ]
            
            if "drider_eggs" in avatar.ploy:
                self._driders += 1
            
            if self._driders < self.retinue:
                if hasattr(all_actors["alexia"], "job_state") and all_actors["alexia"].job_state.job == "breeding":
                    self._driders += self.drider_recruitment + 0.5
                else:
                    self._driders += self.drider_recruitment
            
            if self._driders > self.retinue:
                if hasattr(all_actors["alexia"], "job_state") and all_actors["alexia"].job_state.job == "breeding":
                    self._driders += self.drider_recruitment + 0.5
                else:
                    self._driders += self.drider_recruitment
                extra = self._driders - self.retinue
                self._driders = self.retinue
                self.reserve += extra
            
            if self._driders == self.retinue:
                if hasattr(all_actors["alexia"], "job_state") and all_actors["alexia"].job_state.job == "breeding":
                    self.reserve += self.drider_recruitment + 0.5
                else:
                    self.reserve += self.drider_recruitment
            
            if self.reserve >  (self.capacity - self.retinue):
                self.reserve =  (self.capacity - self.retinue)
            self.update_tooltip()
        
        def update_tooltip(self):
            
            self.tooltip = ["Check monster report.", f"Drider retinue: {self.driders}/{self.retinue}"]

    class CastleHall(Building):
        '''Castle Hall as a proper class'''
        def __init__(self, uid):
            super(CastleHall, self).__init__(uid)
            self.name = "Castle Hall"
            self.available = True
            self.costs = [0, 300, 400]
            self.capacities = [0, 0, 0]
            self.maintenances = [25, 30, 40]
            self.incomes = [50, 70, 90]
            self.researches = [0, 0, 0]
            self.recruitments = [0, 0, 0]
            self.morales = [3, 3.5, 4]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_ThroneRoom.png'
            self.prereqs = [
                ["Already built"],
                ["Requires Technology: Opulence"],
                ["Requires Technology: Dark dynasty"]
            ]
            self.perks = [
                [
                "Weekly income "+str(self.incomes[0]), 
                "Weekly maintenance cost "+str(self.maintenances[0]),
                "Weekly morale "+str(self.morales[0])
                ],
                [
                "Weekly income "+str(self.incomes[0])+"->"+str(self.incomes[1]), 
                "Weekly maintenance cost "+str(self.maintenances[0])+"->"+str(self.maintenances[1]),
                "Weekly morale "+str(self.morales[0])+"->"+str(self.morales[1])
                ],
                [
                "Weekly income "+str(self.incomes[1])+"->"+str(self.incomes[2]), 
                "Weekly maintenance cost "+str(self.maintenances[1])+"->"+str(self.maintenances[2]),
                "Weekly morale "+str(self.morales[1])+"->"+str(self.morales[2])
                ]
            ]
            self.description = "A more impressive court will make our subjects more willing to comply and places us in a better negotiating position.  Restoring the castle's grandeur will not be a simple or inexpensive task, but will certainly have an impact on on the impressionable and those with darkness in their hearts.  It will also allow Jezera to improve and upgrade the general infrastructure of the entire surface half of the castle."
            self.lvl = 0
            self.max_lvl = 1
            self.build()
        
        def weekly(self):
            self.update_tooltip()
        
        def update_tooltip(self):
            
            self.tooltip = ["Check current objectives and realm reports.", f"Added income: {self.income-self.maintenance}", f"Added morale: {self.morale}"]

    class Library(Building):
        '''Library as a proper class'''
        def __init__(self, uid):
            super(Library, self).__init__(uid)
            self.name = "Library"
            self.available = True
            self.costs = [200, 350, 450]
            self.capacities = [0, 0, 0]
            self.maintenances = [0, 10, 20]
            self.incomes = [0, 0, 0]
            self.researches = [10, 12.5, 15]
            self.recruitments = [0, 0, 0]
            self.morales = [0, 0, 0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Library.png'
            self.prereqs = [
                ["Already built at level 1"],
                ["Requires Technology: Tools and Schematics"],
                ["Requires Technology: Grand Projects"]
            ]
            self.perks = [
                [
                "Weekly maintenance cost "+str(self.maintenances[0]), 
                "Weekly research "+str(self.researches[0])+" RP"
                ],
                [
                "Weekly maintenance cost "+str(self.maintenances[0])+"->"+str(self.maintenances[1]), 
                "Weekly research "+str(self.researches[0])+" RP ->"+str(self.researches[1])+" RP"
                ],
                [
                "Weekly maintenance cost "+str(self.maintenances[1])+"->"+str(self.maintenances[2]), 
                "Weekly research "+str(self.researches[1])+" RP ->"+str(self.researches[2])+" RP"
                ]
            ]
            self.description = "The Bloodmeen library is one of the most extensive and well stocked collections in the whole of the Six Realms.  Cliohna has taken possession of it and uses it for both her own personal projects and as the center of operations for the magic and research projects of the castle. Expanding on the collection of books available must be done by finding libraries and abbeys in the world.\n However, what can be done here is investing our treasury into expanded laboratory facilities, equipment, and training staff for the library. These will allow Cliohna to both handle more magical related infrastructure in the castle and expand the scope of her research on Bloodmeen's behalf."
            self.lvl = 0
            self.max_lvl = 1
            self.build()
        
        def weekly(self):
            self.update_tooltip()
        
        def update_tooltip(self):
            
            self.tooltip = ["Change current research.", f"Added research: {self.research}"]

    class Tavern(Building):
        '''Tavern as a proper class'''
        def __init__(self, uid):
            super(Tavern, self).__init__(uid)
            self.name = "Tavern"
            self.available = True
            self.costs = [150, 250, 450]
            self.capacities = [0, 0, 0]
            self.maintenances = [0, 0, 0]
            self.incomes = [30, 60, 90]
            self.researches = [0, 0, 0]
            self.recruitments = [0, 0, 0]
            self.morales = [0, 0, 0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Tavern.png'
            self.prereqs = [
                ["Immediately available to build at level 1"],
                ["Requires technology: Silks and Smiles"], 
                ["Requires technology: The Value of Gossip"]
            ]
            self.perks = [
                ["Weekly income "+str(self.incomes[0])],
                ["Weekly income "+str(self.incomes[0])+"->"+str(self.incomes[1])],
                ["Weekly income "+str(self.incomes[1])+"->"+str(self.incomes[2])]
            ]
            self.description = "Unlike most of the buildings we are building here, the tavern is not going to be on the castle grounds at all. In fact, the tavern will be constructed near a portal site in the middle of the Rakshan Wastes. This has been the site of numerous rest posts, taverns, and bases over the centuries for travellers and caravans making the difficult overland journey between Qerazel and Ealoean. Generally it has been abandoned either due to demon wars or the difficulty in bringing supplies. The portals will make it much cheaper for us to maintain, while still allowing us to charge top prices for food, drinks, and services.\n Jezera has made the acquaintance of a woman from the Dragon's Tail with great experience working tables of such places who is eager to have a place of her own. Baring unexpected circumstances, she will be brought to the castle once the tavern has been constructed."
            self.lvl = 0
            self.max_lvl = 1
        
        def weekly(self):
            self.update_tooltip()
        
        def update_tooltip(self):
            
            self.tooltip = [f"Added income: {self.income}"]

    class Quarters(Building):
        '''Quarters as a proper class.  Shows as having two levels but lvl 2 not in game at the moment'''
        def __init__(self, uid):
            super(Quarters, self).__init__(uid)
            self.name = "Living Quarters"
            self.available = False
            self.costs = [0,0,0]
            self.capacities = [0,0,0]
            self.maintenances = [5,5,5]
            self.incomes = [0,0,0]
            self.researches = [0,0,0]
            self.recruitments = [0,0,0]
            self.morales = [0,0,0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_LivingQuarters.png'
            self.prereqs = [["Already built"],[""],[""]]
            self.perks = [[""],[""],[""]]
            self.description = ""
            self.lvl = 0
            self.max_lvl = 1
            self.build()

    class Caravan(Building):
        '''Caravan as a proper class.  Looks like a wagon is a building when it is stalled.  Second tier not currently in the game'''
        def __init__(self, uid):
            super(Caravan, self).__init__(uid)
            self.name = "Caravan"
            self.available = False
            self.costs = [0, 300,0]
            self.capacities = [0, 0,0]
            self.maintenances = [0, 0,0]
            self.incomes = [0, 0,0]
            self.researches = [0, 0,0]
            self.recruitments = [0, 0,0]
            self.morales = [0, 0,0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Wagon.png'
            self.prereqs = [["Already built"],[""],[""]]
            self.perks = [[""],[""],[""]]
            self.description = ""
            self.lvl = 0
            self.max_lvl = 1
            self.build()


    class Kennel(Building):
        '''Kennel as a proper class.  Not in the game yet'''
        def __init__(self, uid):
            super(Kennel, self).__init__(uid)
            self.name = "Warg Kennel"
            self.available = False
            self.costs = [250,0,0]
            self.capacities = [0,0,0]
            self.maintenances = [0,0,0]
            self.incomes = [0,0,0]
            self.researches = [0,0,0]
            self.recruitments = [0,0,0]
            self.morales = [0,0,0]
            self.thumbnail = None
            self.prereqs = [["Requires Technology: Monster Taming"],[""],[""]]
            self.perks = [[""],[""],[""]]
            self.description = ""
            self.lvl = 0
            self.max_lvl = 0

    class Arena(Building):
        '''Arena as a proper class'''
        def __init__(self, uid):
            super(Arena, self).__init__(uid)
            self.name = "Arena"
            self.available = True
            self.costs = [200, 250, 300]
            self.capacities = [0, 0, 0]
            self.maintenances = [20, 40, 60]
            self.incomes = [0, 0, 0]
            self.researches = [0, 0, 0]
            self.recruitments = [0, 0, 0]
            self.morales = [2, 4, 6]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Arena.png'
            self.prereqs = [
                ["Requires Technology: Ordering Chaos"],
                ["Requires Technology: Military Logistics"],
                ["Requires Technology: Tribe Negotiations"]
            ]
            self.perks = [
                [
                "Weekly maintenance "+str(self.maintenances[0]), 
                "Weekly morale boost "+str(self.morales[0])
                ],
                [
                "Weekly maintenance "+str(self.maintenances[0])+"->"+str(self.maintenances[1]), 
                "Weekly morale boost "+str(self.morales[0])+"->"+str(self.morales[1])
                ],
                [
                "Weekly maintenance "+str(self.maintenances[1])+"->"+str(self.maintenances[2]), 
                "Weekly morale boost "+str(self.morales[1])+"->"+str(self.morales[2])
                ],
            ]
            self.description =  "As the armies of the twins grow larger, they also grow more restless.  A fighting arena will provide the perfect place to blow off steam and keep spirits up.  However, this expensive facility will not provide many other benefits and should only be considered for construction if morale becomes a problem.\n Andras plans on taking personal management of the arena once it has been completed."
            
            self.lvl = 0
            self.max_lvl = 0
        
        def weekly(self):
            self.update_tooltip()
        
        def update_tooltip(self):
            
            self.tooltip = [f"Added morale: {self.morale}"]

    class Summoning(Building):
        '''Summoning as a proper class'''
        def __init__(self, uid):
            super(Summoning, self).__init__(uid)
            self.name = "Summoning Chambers"
            self.available = False
            self.costs = [300, 600, 900]
            self.capacities = [0, 0, 0]
            self.maintenances = [10, 10, 10]
            self.incomes = [0, 0, 0]
            self.researches = [1, 2, 3]
            self.recruitments = [0, 0, 0]
            self.morales = [0, 0, 0]
            self.thumbnail = None
            self.prereqs = [["Requires Technology: Basic Summoning"],[""],[""]]
            self.perks = [[""],[""],[""]]
            self.description = ""
            self.lvl = 0
            self.max_lvl = 0

    class Workshop(Building):
        '''Workshop as a proper class'''
        def __init__(self, uid):
            super(Workshop, self).__init__(uid)
            self.name = "Workshop"
            self.available = False
            self.costs = [0, 200, 400]
            self.capacities = [0, 0, 0]
            self.maintenances = [0, 0, 0]
            self.incomes = [0, 0, 0]
            self.researches = [0, 0, 0]
            self.recruitments = [0, 0, 0]
            self.morales = [0, 0, 0]
            self.thumbnail = 'gui/Thumbnail UI images/Icon_Workshop_Workshop.png'
            self.prereqs = [["Aleady built and not upgradable"],[""],[""]]
            self.perks = [[""],[""],[""]]
            self.description = "This room, which serves as my planning and drafting room for all construction projects as well as ongoing excavations of the castle tunnels. This space is also where I tend to my hobbies and keep my tools.  Most of the actual work for any building projects will take place on-site, so upgrades and improvements to this building will be unnecessary."
            self.lvl = 0
            self.max_lvl = 1
            self.tooltip = ["Construct or upgrade buildings in the castle."]
            self.update_tooltip()
            self.build()
        def update_tooltip(self):
            
            self.tooltip = ["Construct or upgrade buildings in the castle."]

    class NasimChamber(Building):
        '''NasimChamber as a proper class'''
        def __init__(self, uid):
            super(NasimChamber, self).__init__(uid)
            self.name = "Nasim Chamber"
            self.available = False
            self.costs = [80]
            self.capacities = [0]
            self.maintenances = [0]
            self.incomes = [0]
            self.researches = [2]
            self.recruitments = [0]
            self.morales = [0]
            self.thumbnail = None
            self.prereqs = [["Meet Nasim for the first time"]]
            self.perks = [
                [
                "Weekly research "+str(self.researches[0])+" RP", 
                "Furthers Nasim's Nasim’s Transformation research"
                ]
            ]
            self.description = "Built by Demon Lord Talmoth centuries ago, this mystical chamber focuses chaos energies, allowing for arcane feats that far surpass conventional magic. Lying deep beneath Castle Bloodmeen, it must be excavated before Nasim can begin restoring it."
            
            self.lvl = 0
            self.max_lvl = 0

    class MagicBuilding(Building):
        def __init__(self, uid):
            super(MagicBuilding, self).__init__(uid)


    all_buildings = {
        'hall': CastleHall,
        'library': Library,
        'barracks': Barracks,
        'dungeon': Dungeon,
        'sanctum': DarkSanctum,
        'tavern': Tavern,
        'forge': Forge,
        'quarters': Quarters,
        'caravan': Caravan,
        'workshop': Workshop,
        'kennel': Kennel,
        'pit': BreedingPit,
        'brothel': Brothel,
        'arena': Arena,
        'summoning': Summoning,
        'nasim_chamber': NasimChamber
        }
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
