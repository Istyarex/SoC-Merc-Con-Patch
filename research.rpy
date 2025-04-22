

init python:

    class Research(object):
        '''Base class for researches'''
        uid = 'BASE'
        name = 'BASE'
        category = 'BASE'
        completed = False
        cost = 0
        rp_spent = 0
        thumbnail = 'gui/Thumbnail UI images/UI_Research_ToolsSchematics.png' 
        
        requires = 'nothing'
        
        unlocks = 'nothing'
        
        
        def req_met(self):
            '''Returns True if all requirements are met'''
            
            return True
        
        def on_complete(self):
            '''This runs once when the research is completed'''
            castle.completed_researches.append(uid)
            castle.researches[uid].completed = True
            pass


    class WorldAndTheWar(Research):
        uid = 'world_and_the_war'
        name = 'World and the War'
        category = 'history'
        cost = 40
        unlocks = 'Background info, choices in events.'
        
        def req_met(self):
            return False


    class HistoryOfRosaria(Research):
        uid = 'history_of_rosaria'
        name = 'History of Rosaria'
        category = 'exploration'
        cost = 50
        unlocks = 'Background info, Todo: choices in events.'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_HistoryOfRosaria.png' 
        
        def on_complete(self):
            avatar.add_exp(200)

    class MilitaryTactics(Research):
        uid = 'military_tactics'
        name = 'Military Tactics'
        category = 'military'
        cost = 40
        unlocks = 'Level 2 barracks'
        
        def req_met(self):
            
            return False
        
        def on_complete(self):
            castle.buildings['barracks'].max_lvl = 2


    class MilitaryLogistics(Research):
        uid = 'military_logistics'
        name = 'Military Logistics'
        category = 'military'
        cost = 70
        requires = 'Ordering chaos'
        unlocks = 'Level 3 barracks, level 2 arena, reduce orc treasury upkeep by 10%'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_MilitaryLogistics.png'
        
        def req_met(self):
            return castle.researches['ordering_chaos'].completed 
        
        def on_complete(self):
            castle.buildings['barracks'].max_lvl = 3
            castle.buildings['arena'].max_lvl = 2
            all_troops['orc']['maintenance']-=0.1


    class MilitaryRecreation(Research):
        uid = 'military_recreation'
        name = 'Military Recreation'
        category = 'military'
        cost = 100
        requires = 'Military tactics'
        unlocks = 'Level 2 arena'
        
        def req_met(self):
            
            return False
        
        
        def on_complete(self):
            castle.buildings['arena'].max_lvl = 2


    class SurvivalismAndCartography(Research):
        uid = 'survivalism_and_cartography'
        name = 'Survivalism and Cartography'
        category = 'exploration'
        cost = 50
        unlocks = 'Extra movement on map and/or reduced cost in explored.'
        
        def req_met(self):
            
            return False
        
        def on_complete(self):
            avatar._base_mp += 1


    class AdvancedSurvivalTechniques(Research):
        uid = 'advanced_survival_techniques'
        name = 'Advanced Survival Techniques'
        category = 'exploration'
        cost = 100
        requires = 'Survivalism and cartography'
        unlocks = 'Extra movement on map and/or reduced cost in explored.'
        
        def req_met(self):
            
            return False



    class SurveyingAndTelescopics(Research):
        uid = 'surveying_and_telescopics'
        name = 'Surveying and Telescopics'
        category = 'exploration'
        cost = 100
        unlocks = 'Increases visible hex range to 2.'
        
        def req_met(self):
            
            return False
        
        
        def on_complete(self):
            avatar.view_distance = 2


    class AdvancedTelescopics(Research):
        uid = 'advanced_telescopics'
        name = 'Advanced Telescopics'
        category = 'exploration'
        cost = 100
        requires = 'Telescopics'
        unlocks = 'Increases visible hex range to 3.'
        
        def req_met(self):
            
            return False



    class Excavation(Research):
        uid = 'excavation'
        name = 'Excavation'
        category = 'resources'
        cost = 60
        requires = 'Claim a mine'
        unlocks = 'Increase to mine resource yield.'
        
        def req_met(self):
            
            return False


    class AdvancedExtraction(Research):
        uid = 'advanced_extraction'
        name = 'Advanced Extraction'
        category = 'resources'
        cost = 100
        requires = 'Excavation'
        unlocks = 'Further increase to mine resource yield.'
        
        def req_met(self):
            
            return False



    class LaborPlanning(Research):
        uid = 'labor_planning'
        name = 'Labor Planning'
        category = 'resources'
        cost = 60
        requires = 'Occupy a second village'
        unlocks = 'Increase to occupied village income yield.'
        
        def req_met(self):
            
            return False


    class Colonialism(Research):
        uid = 'colonialism'
        name = 'Colonialism'
        category = 'resources'
        cost = 100
        requires = 'Labor planning'
        unlocks = 'Further increase to occupied village income yield.'
        
        def req_met(self):
            
            return False



    class TradeRoutes(Research):
        uid = 'trade_routes'
        name = 'Trade Routes'
        category = 'resources'
        cost = 60
        requires = 'Tavern'
        unlocks = 'Increase to village trade yield.'
        
        def req_met(self):
            
            return False



    class ImprovedLogistics(Research):
        uid = 'improved_logistics'
        name = 'Improved Logistics'
        category = 'resources'
        cost = 100
        requires = 'Trade routes'
        unlocks = 'Further increase to village trade yield.'
        
        def req_met(self):
            
            return False



    class MonsterTaming(Research):
        uid = 'monster_taming'
        name = 'Monster Taming'
        category = 'monsters'
        cost = 25
        unlocks = 'Breeding pit'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_MonsterTaming.png' 
        
        def on_complete(self):
            castle.buildings['pit'].max_lvl = 1


    class MonsterHandling(Research):
        uid = 'monster_handling'
        name = 'Monster Handling'
        category = 'monsters'
        cost = 160
        requires = 'Monster taming, breeding pit'
        unlocks = 'Can breed medium sized monsters.'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_MonsterTaming.png'
        
        def req_met(self):
            
            return False



    class MonsterZoology(Research):
        uid = 'monster_zoology'
        name = 'Monster Zoology'
        category = 'monsters'
        cost = 120
        requires = 'Monster taming, breeding pit'
        unlocks = 'Level 2 breeding pit'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_MonsterTaming.png' 
        
        def req_met(self):
            
            return False
        
        
        def on_complete(self):
            castle.buildings['pit'].max_lvl = 2


    class SpecialHandlingTechniques(Research):
        uid = 'special_handling_techniques'
        name = 'Special Handling Techniques'
        category = 'monsters'
        cost = 240
        requires = 'Monster handling, monster zoology'
        unlocks = 'Can breed large sized monsters.'
        
        def req_met(self):
            
            return False



    class Opulence(Research):
        uid = 'opulence'
        name = 'Opulence'
        category = 'splendour'
        cost = 70
        unlocks = 'Level 2 castle hall, level 2 dark sanctum, reduce cubi sorcerer treasury upkeep by 10%, to 90%'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_Opulence.png' 
        
        def on_complete(self):
            castle.buildings['hall'].max_lvl = 2
            castle.buildings['sanctum'].max_lvl = 2
            all_troops['cubi']['maintenance']-=0.3



    class FiendishDiplomacy(Research):
        uid = 'fiendish_diplomacy'
        name = 'Fiendish Diplomacy'
        category = 'diplomacy'
        cost = 40
        unlocks = 'Level 1 brothel'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_FiendishDiplomacy.png' 
        
        def on_complete(self):
            castle.buildings['brothel'].max_lvl = 1


    class DarkSubterfuge(Research):
        uid = 'dark_subterfuge'
        name = 'Dark Subterfuge'
        category = 'diplomacy'
        cost = 60
        requires = 'Opulence'
        unlocks = 'Brothel'
        
        def req_met(self):
            
            return False
        
        
        def on_complete(self):
            castle.buildings['brothel'].max_lvl = 1


    class SilksAndSmiles(Research):
        uid = 'silks_and_smiles'
        name = 'Silks and Smiles'
        category = 'diplomacy'
        cost = 70
        requires = 'Fiendish diplomacy, and either level 1 brothel or level 1 tavern'
        unlocks = 'Level 2 brothel, level 2 tavern, +10% spy efficiency'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_SilksAndSmiles.png' 
        
        def req_met(self):
            return castle.researches['fiendish_diplomacy'].completed and (castle.buildings['brothel'].lvl >= 1 or castle.buildings['tavern'].lvl >= 1)
        
        def on_complete(self):
            castle.buildings['brothel'].max_lvl = 2
            castle.buildings['tavern'].max_lvl = 2
            castle.buildings['brothel'].military_effectiveness += 0.1
            castle.buildings['brothel'].blackmail_effectiveness += 0.1
            castle.buildings['brothel'].kidnapping_effectiveness += 0.1


    class ContactNetwork(Research):
        uid = 'contact_network'
        name = 'Contact Network'
        category = 'research and magic'
        cost = 80
        unlocks = 'Level 2 library, level 2 dark sanctum'
        
        def req_met(self):
            
            return False
        
        def on_complete(self):
            castle.buildings['library'].max_lvl = 2
            castle.buildings['sanctum'].max_lvl = 2


    class BasicSummoning(Research):
        uid = 'basic_summoning'
        name = 'Basic Summoning'
        category = 'research and magic'
        cost = 60
        requires = 'Contact network'
        unlocks = 'Summoning Chambers'
        
        def req_met(self):
            
            return False
        
        
        def on_complete(self):
            castle.buildings['summoning'].max_lvl = 1


    class Demonology(Research):
        uid = 'demonology'
        name = 'Demonology'
        category = 'research and magic'
        cost = 240
        requires = 'Basic summoning, summoning chambers'
        unlocks = 'Can summon demons'
        
        def req_met(self):
            
            return False



    class Smelting(Research):
        uid = 'smelting'
        name = 'Smelting'
        category = 'metalwork'
        cost = 100
        unlocks = 'Level 2 forge'
        
        def req_met(self):
            
            return False
        
        
        def on_complete(self):
            castle.buildings['forge'].max_lvl = 2


    class TheRiddleOfSteel(Research):
        uid = 'the_riddle_of_steel'
        name = 'The Riddle of Steel'
        category = 'research and metalwork'
        cost = 40
        requires = 'Smelting'
        unlocks = 'Allows steel equipment to be made from iron'
        
        def req_met(self):
            
            return False





    class ResearchInfrastructure(Research):
        uid = "research_infrastructure"
        name = "Research Infrastructure"
        category = "research and magic"
        cost = 140
        unlocks = 'Level 3 Library and Level 1 Arena'
        
        def req_met(self):
            
            return False
        
        
        def on_complete(self):
            castle.buildings['library'].max_lvl = 3

    class OrderingChaos(Research):
        uid = "ordering_chaos"
        name = "Ordering Chaos"
        category = "military"
        cost = 40
        unlocks = 'Level 2 Barracks, Level 1 Arena'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_OrderingChaos.png' 
        
        def on_complete(self):
            castle.buildings['barracks'].max_lvl = 2
            castle.buildings['arena'].max_lvl = 1

    class TheValueOfGossip(Research):
        uid = "the_value_of_gossip"
        name = "The Value of Gossip"
        category = "diplomacy"
        cost = 100
        requires = 'Silks and Smiles, and either Level 2 tavern or Level 2 brothel'
        unlocks = 'Level 3 tavern and Level 3 brothel, +10% spy efficiency'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_TheValueOfGossip.png' 
        
        def req_met(self):
            return castle.researches['silks_and_smiles'].completed and (castle.buildings['tavern'].lvl >= 2 or castle.buildings['brothel'].lvl >= 2 )
        
        def on_complete(self):
            castle.buildings['tavern'].max_lvl = 3
            castle.buildings['brothel'].max_lvl = 3
            castle.buildings['brothel'].military_effectiveness += 0.1
            castle.buildings['brothel'].blackmail_effectiveness += 0.1
            castle.buildings['brothel'].kidnapping_effectiveness += 0.1

    class MercenaryContracts(Research):
        uid = "mercenary_contracts"
        name = "Mercenary Contracts"
        category = "diplomacy"
        cost = 60
        requires = 'The value of gossip, Level 3 tavern, and Level 3 brothel'
        unlocks = 'Bonus to Military Espionage, +10%, Todo: Army Score: +350'
        
        def req_met(self):
            return castle.researches['the_value_of_gossip'].completed and castle.buildings['tavern'].lvl >= 3 and castle.buildings['brothel'].lvl >= 3
        
        def on_complete(self):
            brothel = castle.buildings['brothel']
    
            if not hasattr(brothel, 'research_military_bonus'):
                brothel.research_military_bonus = 0

            brothel.research_military_bonus += 0.1
            brothel.military_effectiveness += 0.1



    class TribeNegotiations(Research):
        uid = "tribe_negotiations"
        name = "Tribe Negotiations"
        category = "military"
        cost = 100
        requires = 'Military Logistics'
        unlocks = 'Level 4 barracks, level 3 arena, further reduce orc treasury upkeep by 10%, to 80%'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_TribeNegotiation.png' 
        
        def req_met(self):
            return castle.researches['military_logistics'].completed
        
        def on_complete(self):
            castle.buildings['barracks'].max_lvl = 4
            castle.buildings['arena'].max_lvl = 3
            all_troops['orc']['maintenance'] -= 0.1

    class SurvivalOfTheFittest(Research):
        uid = "survival_of_the_fittest"
        name = "Survival of the Fittest"
        category = "military"
        cost = 100
        requires = 'Tribe Negotiations, Level 2 barracks'
        unlocks = '+2 orc military power'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_SurvivaloftheFittest.png' 
        
        def req_met(self):
            return castle.researches['tribe_negotiations'].completed and castle.buildings['barracks'].lvl >= 2
        
        def on_complete(self):
            all_troops['orc']['strength'] += 2

    class ToolsAndSchematics(Research):
        uid = "tools_and_schematics"
        name = "Tools and Schematics"
        category = "research and metalwork"
        cost = 70
        unlocks = 'Level 2 library, Level 2 forge'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_ToolsSchematics.png' 
        
        def on_complete(self):
            castle.buildings['library'].max_lvl = 2
            castle.buildings['forge'].max_lvl = 2

    class GrandProjects(Research):
        uid = "grand_projects"
        name = "Grand Projects"
        category = "research and metalwork"
        cost = 100
        requires = 'Tools and schematics, Level 2 library or Level 2 forge'
        unlocks = 'Level 3 library, Level 3 forge'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_GrandProjects.png' 
        
        def req_met(self):
            return castle.researches['tools_and_schematics'].completed and (castle.buildings['library'].lvl >= 2 or castle.buildings['forge'].lvl >= 2 )
        
        def on_complete(self):
            castle.buildings['library'].max_lvl = 3
            castle.buildings['forge'].max_lvl = 3

    class DriderTraining(Research):
        uid = "drider_training"
        name = "Drider Training"
        category = "monsters"
        cost = 50
        requires = 'Monster taming, Level 1 breeding pit'
        unlocks = 'Level 2 breeding pit, reduce drider treasury upkeep by 10%, to 90%'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_DriderTraining.png'
        
        def req_met(self):
            return castle.researches['monster_taming'].completed and castle.buildings['pit'].lvl >= 1
        
        def on_complete(self):
            castle.buildings['pit'].max_lvl = 2
            all_troops['drider']['maintenance']-=0.4

    class DriderNaturalisation(Research):
        uid = "drider_naturalisation"
        name = "Drider Naturalisation"
        category = "monsters"
        cost = 60
        requires = 'Drider training, Level 2 breeding pit'
        unlocks = 'Level 3 breeding pit, further reduce drider treasury upkeep by 10%, to 80%'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_DriderNaturalization.png'
        
        def req_met(self):
            return castle.researches['drider_training'].completed and castle.buildings['pit'].lvl >= 2
        
        def on_complete(self):
            castle.buildings['pit'].max_lvl = 3
            all_troops['drider']['maintenance']-=0.4

    class TheDomesticizedAlphaParadox(Research):
        uid = "the_domesticized_alpha_paradox"
        name = "The Domesticized Alpha Paradox"
        category = "monsters"
        cost = 60
        requires = 'Drider naturalisation, Level 3 breeding pit'
        unlocks = '+5 drider military power'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_DomesticizedAlphaParadox.png'
        
        def req_met(self):
            return castle.researches['drider_naturalisation'].completed and castle.buildings['pit'].lvl >= 3
        
        def on_complete(self):
            all_troops['drider']['strength'] += 5

    class DarkDynasty(Research):
        uid = "dark_dynasty"
        name = "Dark Dynasty"
        category = "splendour"
        cost = 100
        requires = 'Opulence, Level 2 castle hall or Level 2 dark sanctum'
        unlocks = 'Level 3 castle hall, Level 3 dark sanctum, further reduce cubi sorcerer treasury upkeep by 10%, to 80%'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_DarkDynasty.png'
        
        def req_met(self):
            return castle.researches['opulence'].completed and (castle.buildings['hall'].lvl >= 2 or castle.buildings['sanctum'].lvl >= 2 )
        
        def on_complete(self):
            castle.buildings['hall'].max_lvl = 3
            castle.buildings['sanctum'].max_lvl = 3
            all_troops['cubi']['maintenance']-=0.3

    class EvolutionThroughDiscord(Research):
        uid = "evolution_through_discord"
        name = "Evolution Through Discord"
        category = "splendour"
        cost = 70
        requires = 'Dark dynasty and Level 3 dark sanctum'
        unlocks = '+4 cubi sorcerer military power, +0.05 cubi sorcerer weekly morale, +10% spy effiency'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_EvolutionThroughDiscord.png'
        
        def req_met(self):
            return castle.researches['dark_dynasty'].completed and castle.buildings['sanctum'].lvl >= 3
        
        def on_complete(self):
            all_troops['cubi']['strength'] += 4
            all_troops['cubi']['morale_cost'] -= 0.05
            castle.buildings['brothel'].military_effectiveness += 0.1
            castle.buildings['brothel'].blackmail_effectiveness += 0.1
            castle.buildings['brothel'].kidnapping_effectiveness += 0.1

    class ProspectingForResources(Research):
        uid = "prospecting_for_resources"
        name = "Prospecting for Resources"
        category = "diplomacy"
        cost = 60
        
        def req_met(self):
            
            return False

    class HeroicTraining(Research):
        uid = "heroic_training"
        name = "Heroic Training"
        category = "diplomacy"
        cost = 60
        
        def req_met(self):
            
            return False

    class AwakenTheDawnStar(Research):
        uid = "awaken_the_dawn_star"
        name = "Awaken the Dawn Star"
        category = "diplomacy"
        cost = 60
        
        def req_met(self):
            
            return False

    class StalkersInTheNight(Research):
        uid = "stalkers_in_the_night"
        name = "Stalkers in the Night"
        category = "splendour"
        cost = 40
        requires = 'Opulence, Level 2 dark sanctum, and Level 1 brothel'
        unlocks = 'Bonus to Kidnapping (10%), Weekly prisoners +1'
        thumbnail = 'gui/Thumbnail UI images/UI_Research_Opulence.png'
        
        def req_met(self):
            return castle.researches['opulence'].completed and castle.buildings['sanctum'].lvl >= 2 and castle.buildings['brothel'].lvl >= 1
        
        def on_complete(self):
            castle.buildings['brothel'].kidnapping_effectiveness += 0.1


    all_researches = [WorldAndTheWar, HistoryOfRosaria, MilitaryTactics, MilitaryLogistics, MilitaryRecreation, SurvivalismAndCartography,
        AdvancedSurvivalTechniques, SurveyingAndTelescopics, AdvancedTelescopics, Excavation, AdvancedExtraction, LaborPlanning, Colonialism,
        TradeRoutes, ImprovedLogistics, MonsterTaming, MonsterHandling, MonsterZoology, SpecialHandlingTechniques, Opulence, FiendishDiplomacy,
        DarkSubterfuge, SilksAndSmiles, ContactNetwork, BasicSummoning, Demonology, Smelting, TheRiddleOfSteel, ResearchInfrastructure, OrderingChaos, 
        TheValueOfGossip, MercenaryContracts, TribeNegotiations, SurvivalOfTheFittest, ToolsAndSchematics, GrandProjects, DriderTraining, 
        DriderNaturalisation, TheDomesticizedAlphaParadox, DarkDynasty, EvolutionThroughDiscord, ProspectingForResources, HeroicTraining, 
        AwakenTheDawnStar, StalkersInTheNight]



    all_research_categories = ['history', 'military', 'exploration', 'resources', 'monsters', 'diplomacy', 'research and magic', 'metalwork', 'research and metalwork', 'splendour' ]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
