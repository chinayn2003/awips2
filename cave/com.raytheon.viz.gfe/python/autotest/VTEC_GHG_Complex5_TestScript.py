##
# This software was developed and / or modified by Raytheon Company,
# pursuant to Contract DG133W-05-CQ-1067 with the US Government.
# 
# U.S. EXPORT CONTROLLED TECHNICAL DATA
# This software product contains export-restricted data whose
# export/transfer/disclosure is restricted by U.S. law. Dissemination
# to non-U.S. persons whether in the United States or abroad requires
# an export license or other authorization.
# 
# Contractor Name:        Raytheon Company
# Contractor Address:     6825 Pine Street, Suite 340
#                         Mail Stop B8
#                         Omaha, NE 68106
#                         402.291.0100
# 
# See the AWIPS II Master Rights File ("Master Rights File.pdf") for
# further licensing information.
##
# ----------------------------------------------------------------------------
# This software is in the public domain, furnished "as is", without technical
# support, and with no warranty, express or implied, as to its usefulness for
# any purpose.
#
# More VT?EC_GHG Complex Hazard Tests 
#
# Author:
# ----------------------------------------------------------------------------

scripts = [
    {
    "commentary": "Clear out all Hazards Table and Grids.", 
    "name": "GHG_Complex5_0",
    "productType": None,
    "clearHazardsTable": 1,
    "checkStrings": [],
    },
    {
    
    "commentary": """
    Creating a WS.A hazard for Area1, Area2, Area3, and Area4
    Note that the ETN number illustrates the Area (:1, :2, :3, :4)
    During this run Area3 and Area4 are combined into the same segment
    Area1 (FLZ039, FLZ142, FLZ242) 24-53
    Area2 (FLZ052) 24-53
    Area3 (FLZ061) 24-53
    Area4 (FLZ162, FLZ262) 24-53
    """,
    
    "name": "GHG_Complex5_1",
    "productType": "Hazard_WSW_Local",
    "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
        ("Fcst", "Hazards", "DISCRETE", 24, 53, "WS.A:1", ["FLZ139", "FLZ239", "FLZ142", "FLZ242"]),
        ("Fcst", "Hazards", "DISCRETE", 24, 53, "WS.A:2", ["FLZ052"]),
        ("Fcst", "Hazards", "DISCRETE", 24, 53, "WS.A:3", ["FLZ061", "FLZ162", "FLZ262"]),
        ],
    "checkStrings": [
      "WWUS42 KTBW 010000",
      "WSWTBW",
      "URGENT - WINTER WEATHER MESSAGE",
      "National Weather Service Tampa Bay Ruskin FL",
      "700 PM EST Thu Dec 31 2009",
      "...|*Overview headline (must edit)*|...",
      ".|*Overview (must edit)*|.",
      "FLZ139-142-239-242-010800-",
      "/O.NEW.KTBW.WS.A.0001.100102T0000Z-100103T0500Z/",
      "Coastal Levy-Coastal Citrus-Inland Levy-Inland Citrus-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WATCH IN EFFECT FROM FRIDAY EVENING THROUGH SATURDAY EVENING...",
      "The National Weather Service in Tampa Bay Ruskin has issued a Winter Storm Watch...which is in effect from Friday evening through Saturday evening. ",
#      "|* SEGMENT TEXT GOES HERE *|.",
      "Precautionary/preparedness actions...",
      "A Winter Storm Watch means there is a potential for significant snow...sleet...or ice accumulations that may impact travel. Continue to monitor the latest forecasts.",
      "&&",
      "$$",
      "FLZ052-010800-",
      "/O.NEW.KTBW.WS.A.0001.100102T0000Z-100103T0500Z/",
      "Polk-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WATCH IN EFFECT FROM FRIDAY EVENING THROUGH SATURDAY EVENING...",
      "The National Weather Service in Tampa Bay Ruskin has issued a Winter Storm Watch...which is in effect from Friday evening through Saturday evening. ",
#       "|* SEGMENT TEXT GOES HERE *|.",
      "Precautionary/preparedness actions...",
      "A Winter Storm Watch means there is a potential for significant snow...sleet...or ice accumulations that may impact travel. Continue to monitor the latest forecasts.",
      "&&",
      "$$",
      "FLZ061-162-262-010800-",
      "/O.NEW.KTBW.WS.A.0001.100102T0000Z-100103T0500Z/",
      "DeSoto-Coastal Charlotte-Inland Charlotte-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WATCH IN EFFECT FROM FRIDAY EVENING THROUGH SATURDAY EVENING...",
      "The National Weather Service in Tampa Bay Ruskin has issued a Winter Storm Watch...which is in effect from Friday evening through Saturday evening. ",
#       "|* SEGMENT TEXT GOES HERE *|.",
      "Precautionary/preparedness actions...",
      "A Winter Storm Watch means there is a potential for significant snow...sleet...or ice accumulations that may impact travel. Continue to monitor the latest forecasts.",
      "&&",
      "$$",
                     ],
    },
    {
    "commentary": "No changes are made to the existing hazards.",
    "name": "GHG_Complex5_2",
    "productType": "Hazard_WSW_Local",
    "deleteGrids": [],
    "checkStrings": [
      "WWUS42 KTBW 010000",
      "WSWTBW",
      "URGENT - WINTER WEATHER MESSAGE",
      "National Weather Service Tampa Bay Ruskin FL",
      "700 PM EST Thu Dec 31 2009",
      "...|*Overview headline (must edit)*|...",
      ".|*Overview (must edit)*|.",
      "FLZ139-142-239-242-010800-",
      "/O.CON.KTBW.WS.A.0001.100102T0000Z-100103T0500Z/",
      "Coastal Levy-Coastal Citrus-Inland Levy-Inland Citrus-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WATCH REMAINS IN EFFECT FROM FRIDAY EVENING THROUGH SATURDAY EVENING...",
#       "A Winter Storm Watch remains in effect from Friday evening through Saturday evening. ",
#      "|* SEGMENT TEXT GOES HERE *|.",
      "Precautionary/preparedness actions...",
      "A Winter Storm Watch means there is a potential for significant snow...sleet...or ice accumulations that may impact travel. Continue to monitor the latest forecasts.",
      "&&",
      "$$",
      "FLZ052-010800-",
      "/O.CON.KTBW.WS.A.0001.100102T0000Z-100103T0500Z/",
      "Polk-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WATCH REMAINS IN EFFECT FROM FRIDAY EVENING THROUGH SATURDAY EVENING...",
#       "A Winter Storm Watch remains in effect from Friday evening through Saturday evening. ",
#      "|* SEGMENT TEXT GOES HERE *|.",
      "Precautionary/preparedness actions...",
      "A Winter Storm Watch means there is a potential for significant snow...sleet...or ice accumulations that may impact travel. Continue to monitor the latest forecasts.",
      "&&",
      "$$",
      "FLZ061-162-262-010800-",
      "/O.CON.KTBW.WS.A.0001.100102T0000Z-100103T0500Z/",
      "DeSoto-Coastal Charlotte-Inland Charlotte-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WATCH REMAINS IN EFFECT FROM FRIDAY EVENING THROUGH SATURDAY EVENING...",
#       "A Winter Storm Watch remains in effect from Friday evening through Saturday evening. ",
#      "|* SEGMENT TEXT GOES HERE *|.",
      "Precautionary/preparedness actions...",
      "A Winter Storm Watch means there is a potential for significant snow...sleet...or ice accumulations that may impact travel. Continue to monitor the latest forecasts.",
      "&&",
      "$$",
                     ],
    },
    {

    "commentary": """
    Upgrading the WS.A hazard to a WS.W hazard in all Areas
    Area2, Area3, and Area4 have new start times
    Area2 (FLZ052) 27-53
    Area3 (FLZ061) 27-53
    Area4 (FLZ162, FLZ262) 36-53
    Note that we had to condense the times into 3 time ranges to accommodate the overlapping
    """,
    
    "name": "GHG_Complex5_3",
    "productType": "Hazard_WSW_Local",
    "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
        ("Fcst", "Hazards", "DISCRETE", 24, 27, "WS.W:1", ["FLZ139", "FLZ239", "FLZ142", "FLZ242"]),
        ("Fcst", "Hazards", "DISCRETE", 27, 36, "WS.W:1", ["FLZ139", "FLZ239", "FLZ142", "FLZ242"]),
        ("Fcst", "Hazards", "DISCRETE", 27, 36, "WS.W:2", ["FLZ052"]),
        ("Fcst", "Hazards", "DISCRETE", 27, 36, "WS.W:3", ["FLZ061"]),
        ("Fcst", "Hazards", "DISCRETE", 36, 53, "WS.W:1", ["FLZ139", "FLZ239", "FLZ142", "FLZ242"]),
        ("Fcst", "Hazards", "DISCRETE", 36, 53, "WS.W:2", ["FLZ052"]),
        ("Fcst", "Hazards", "DISCRETE", 36, 53, "WS.W:3", ["FLZ061"]),
        ("Fcst", "Hazards", "DISCRETE", 36, 53, "WS.W:4", ["FLZ162", "FLZ262"]),
        ],
    "checkStrings": [
      "WWUS42 KTBW 010000",
      "WSWTBW",
      "URGENT - WINTER WEATHER MESSAGE",
      "National Weather Service Tampa Bay Ruskin FL",
      "700 PM EST Thu Dec 31 2009",
      "...|*Overview headline (must edit)*|...",
      ".|*Overview (must edit)*|.",
      "FLZ139-142-239-242-010800-",
      "/O.UPG.KTBW.WS.A.0001.100102T0000Z-100103T0500Z/",
      "/O.NEW.KTBW.WS.W.0001.100102T0000Z-100103T0500Z/",
      "Coastal Levy-Coastal Citrus-Inland Levy-Inland Citrus-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WARNING IN EFFECT FROM 7 PM FRIDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#      "The National Weather Service in Tampa Bay Ruskin has issued a Winter Storm Warning...which is in effect from 7 PM Friday to midnight EST Saturday night. The Winter Storm Watch IS NO LONGER IN EFFECT. ",
#      "|*|* SEGMENT TEXT GOES HERE *|.*|",
      "Precautionary/preparedness actions...",
#      "A Winter Storm Warning MEANS SIGNIFICANT AMOUNTS OF SNOW...SLEET...AND ICE ARE EXPECTED OR OCCURRING. STRONG WINDS ARE ALSO POSSIBLE. THIS WILL MAKE TRAVEL VERY HAZARDOUS OR IMPOSSIBLE.",
      "&&",
      "$$",
      "FLZ052-010800-",
      "/O.UPG.KTBW.WS.A.0001.100102T0000Z-100103T0500Z/",
      "/O.NEW.KTBW.WS.W.0001.100102T0300Z-100103T0500Z/",
      "Polk-",
#       "INCLUDING THE CITIES OF...LAKELAND...WINTER HAVEN",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WARNING IN EFFECT FROM 10 PM FRIDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#      "The National Weather Service in Tampa Bay Ruskin has issued a Winter Storm Warning...which is in effect from 10 PM Friday to midnight EST Saturday night. The Winter Storm Watch IS NO LONGER IN EFFECT. ",
#      "|*|* SEGMENT TEXT GOES HERE *|.*|",
      "Precautionary/preparedness actions...",
#      "A Winter Storm Warning MEANS SIGNIFICANT AMOUNTS OF SNOW...SLEET...AND ICE ARE EXPECTED OR OCCURRING. STRONG WINDS ARE ALSO POSSIBLE. THIS WILL MAKE TRAVEL VERY HAZARDOUS OR IMPOSSIBLE.",
      "&&",
      "$$",
      "FLZ061-010800-",
      "/O.UPG.KTBW.WS.A.0001.100102T0000Z-100103T0500Z/",
      "/O.NEW.KTBW.WS.W.0001.100102T0300Z-100103T0500Z/",
      "DeSoto-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WARNING IN EFFECT FROM 10 PM FRIDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#      "The National Weather Service in Tampa Bay Ruskin has issued a Winter Storm Warning...which is in effect from 10 PM Friday to midnight EST Saturday night. The Winter Storm Watch IS NO LONGER IN EFFECT. ",
#      "|*|* SEGMENT TEXT GOES HERE *|.*|",
      "Precautionary/preparedness actions...",
#      "A Winter Storm Warning MEANS SIGNIFICANT AMOUNTS OF SNOW...SLEET...AND ICE ARE EXPECTED OR OCCURRING. STRONG WINDS ARE ALSO POSSIBLE. THIS WILL MAKE TRAVEL VERY HAZARDOUS OR IMPOSSIBLE.",
      "&&",
      "$$",
      "FLZ162-262-010800-",
      "/O.UPG.KTBW.WS.A.0001.100102T0000Z-100103T0500Z/",
      "/O.NEW.KTBW.WS.W.0001.100102T1200Z-100103T0500Z/",
      "Coastal Charlotte-Inland Charlotte-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WARNING IN EFFECT FROM 7 AM SATURDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#      "The National Weather Service in Tampa Bay Ruskin has issued a Winter Storm Warning...which is in effect from 7 AM Saturday to midnight EST Saturday night. The Winter Storm Watch IS NO LONGER IN EFFECT. ",
#      "|*|* SEGMENT TEXT GOES HERE *|.*|",
      "Precautionary/preparedness actions...",
#      "A Winter Storm Warning MEANS SIGNIFICANT AMOUNTS OF SNOW...SLEET...AND ICE ARE EXPECTED OR OCCURRING. STRONG WINDS ARE ALSO POSSIBLE. THIS WILL MAKE TRAVEL VERY HAZARDOUS OR IMPOSSIBLE.",
      "&&",
      "$$",
                     ],
    },
    {
    "commentary": "No changes are made to the existing hazards.",
    "name": "GHG_Complex5_4",
    "productType": "Hazard_WSW_Local",
    "deleteGrids": [],        
    "checkStrings": [
      "WWUS42 KTBW 010000",
      "WSWTBW",
      "URGENT - WINTER WEATHER MESSAGE",
      "National Weather Service Tampa Bay Ruskin FL",
      "700 PM EST Thu Dec 31 2009",
      "...|*Overview headline (must edit)*|...",
      ".|*Overview (must edit)*|.",
      "FLZ139-142-239-242-010800-",
      "/O.CON.KTBW.WS.W.0001.100102T0000Z-100103T0500Z/",
      "Coastal Levy-Coastal Citrus-Inland Levy-Inland Citrus-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WARNING REMAINS IN EFFECT FROM 7 PM FRIDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#       "A Winter Storm Warning remains in effect from 7 PM Friday to midnight EST Saturday night. ",
#      "|*|* SEGMENT TEXT GOES HERE *|.*|",
      "Precautionary/preparedness actions...",
#      "A Winter Storm Warning MEANS SIGNIFICANT AMOUNTS OF SNOW...SLEET...AND ICE ARE EXPECTED OR OCCURRING. STRONG WINDS ARE ALSO POSSIBLE. THIS WILL MAKE TRAVEL VERY HAZARDOUS OR IMPOSSIBLE.",
      "&&",
      "$$",
      "FLZ052-010800-",
      "/O.CON.KTBW.WS.W.0001.100102T0300Z-100103T0500Z/",
      "Polk-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WARNING REMAINS IN EFFECT FROM 10 PM FRIDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#       "A Winter Storm Warning remains in effect from 10 PM Friday to midnight EST Saturday night. ",
#      "|*|* SEGMENT TEXT GOES HERE *|.*|",
      "Precautionary/preparedness actions...",
#      "A Winter Storm Warning MEANS SIGNIFICANT AMOUNTS OF SNOW...SLEET...AND ICE ARE EXPECTED OR OCCURRING. STRONG WINDS ARE ALSO POSSIBLE. THIS WILL MAKE TRAVEL VERY HAZARDOUS OR IMPOSSIBLE.",
      "&&",
      "$$",
      "FLZ061-010800-",
      "/O.CON.KTBW.WS.W.0001.100102T0300Z-100103T0500Z/",
      "DeSoto-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WARNING REMAINS IN EFFECT FROM 10 PM FRIDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#       "A Winter Storm Warning remains in effect from 10 PM Friday to midnight EST Saturday night. ",
#      "|*|* SEGMENT TEXT GOES HERE *|.*|",
      "Precautionary/preparedness actions...",
#      "A Winter Storm Warning MEANS SIGNIFICANT AMOUNTS OF SNOW...SLEET...AND ICE ARE EXPECTED OR OCCURRING. STRONG WINDS ARE ALSO POSSIBLE. THIS WILL MAKE TRAVEL VERY HAZARDOUS OR IMPOSSIBLE.",
      "&&",
      "$$",
      "FLZ162-262-010800-",
      "/O.CON.KTBW.WS.W.0001.100102T1200Z-100103T0500Z/",
      "Coastal Charlotte-Inland Charlotte-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WARNING REMAINS IN EFFECT FROM 7 AM SATURDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#       "A Winter Storm Warning remains in effect from 7 AM Saturday to midnight EST Saturday night. ",
#      "|*|* SEGMENT TEXT GOES HERE *|.*|",
      "Precautionary/preparedness actions...",
#      "A Winter Storm Warning MEANS SIGNIFICANT AMOUNTS OF SNOW...SLEET...AND ICE ARE EXPECTED OR OCCURRING. STRONG WINDS ARE ALSO POSSIBLE. THIS WILL MAKE TRAVEL VERY HAZARDOUS OR IMPOSSIBLE.",
      "&&",
      "$$",
                     ],
    },
    {

    "commentary": """
    Replacing a portion of the WS.W hazard in Area1 with a BZ.W hazard
    Area1 (FLZ142, FLZ242) 24-53
    Replacing the WS.W hazard in Area2 with a WW.Y hazard
    Area2 (FLZ052) 27-53
    """,
    
    "name": "GHG_Complex5_5",
    "productType": "Hazard_WSW_Local",
    "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
        ("Fcst", "Hazards", "DISCRETE", 24, 27, "WS.W:1", ["FLZ139", "FLZ239"]),
        ("Fcst", "Hazards", "DISCRETE", 24, 27, "BZ.W:^WS.W:1", ["FLZ142", "FLZ242"]),
        ("Fcst", "Hazards", "DISCRETE", 27, 36, "WS.W:1", ["FLZ139", "FLZ239"]),
        ("Fcst", "Hazards", "DISCRETE", 27, 36, "BZ.W:^WS.W:1", ["FLZ142", "FLZ242"]),
        ("Fcst", "Hazards", "DISCRETE", 27, 36, "WW.Y", ["FLZ052"]),
        ("Fcst", "Hazards", "DISCRETE", 27, 36, "WS.W:3", ["FLZ061"]),
        ("Fcst", "Hazards", "DISCRETE", 36, 53, "WS.W:1", ["FLZ139", "FLZ239"]),
        ("Fcst", "Hazards", "DISCRETE", 36, 53, "BZ.W:^WS.W:1", ["FLZ142", "FLZ242"]),
        ("Fcst", "Hazards", "DISCRETE", 36, 53, "WW.Y", ["FLZ052"]),
        ("Fcst", "Hazards", "DISCRETE", 36, 53, "WS.W:3", ["FLZ061"]),
        ("Fcst", "Hazards", "DISCRETE", 36, 53, "WS.W:4", ["FLZ162", "FLZ262"]),
        ],
    "checkStrings": [
      "WWUS42 KTBW 010000",
      "WSWTBW",
      "URGENT - WINTER WEATHER MESSAGE",
      "National Weather Service Tampa Bay Ruskin FL",
      "700 PM EST Thu Dec 31 2009",
      "...|*Overview headline (must edit)*|...",
      ".|*Overview (must edit)*|.",
      "FLZ052-010800-",
      "/O.CAN.KTBW.WS.W.0001.100102T0300Z-100103T0500Z/",
      "/O.NEW.KTBW.WW.Y.0001.100102T0300Z-100103T0500Z/",
      "Polk-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER WEATHER ADVISORY IN EFFECT FROM 10 PM FRIDAY TO MIDNIGHT EST SATURDAY NIGHT...",
      "...WINTER STORM WARNING IS CANCELLED...",
#      "The National Weather Service in Tampa Bay Ruskin has issued a Winter Weather Advisory...which is in effect from 10 PM Friday to midnight EST Saturday night. The Winter Storm Warning has been cancelled. ",
#      "|*|*|* SEGMENT TEXT GOES HERE *|.*|*|",
      "Precautionary/preparedness actions...",
#      "A Winter Weather Advisory means that periods of snow...sleet...or freezing rain will cause travel difficulties. Be prepared for slippery roads and limited visibilities...and use caution while driving.",
      "&&",
      "$$",
      "FLZ142-242-010800-",
#     "/O.CAN.KTBW.WS.W.0001.100102T0000Z-100103T0500Z/",
      "/O.UPG.KTBW.WS.W.0001.100102T0000Z-100103T0500Z/",
      "/O.NEW.KTBW.BZ.W.0001.100102T0000Z-100103T0500Z/",
      "Coastal Citrus-Inland Citrus-",
      "700 PM EST Thu Dec 31 2009",
      "...BLIZZARD WARNING IN EFFECT FROM 7 PM FRIDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#       "...WINTER STORM WARNING IS CANCELLED...",
#       "The National Weather Service in Tampa Bay Ruskin has issued a Blizzard Warning...which is in effect from 7 PM Friday to midnight EST Saturday night. The Winter Storm Warning has been cancelled. ",
      "The National Weather Service in Tampa Bay Ruskin has issued a Blizzard Warning...which is in effect from 7 PM Friday to midnight EST Saturday night. The Winter Storm Warning is no longer in effect. ",
#      "|*|*|* SEGMENT TEXT GOES HERE *|.*|*|",
      "Precautionary/preparedness actions...",
      "A Blizzard Warning means severe winter weather conditions are expected or occurring. Falling and blowing snow with strong winds and poor visibilities are likely. This will lead to whiteout conditions...making travel extremely dangerous. Do not travel. If you must travel...have a winter survival kit with you. If you get stranded...stay with your vehicle.",
      "&&",
      "$$",
      "FLZ139-239-010800-",
      "/O.CON.KTBW.WS.W.0001.100102T0000Z-100103T0500Z/",
      "Coastal Levy-Inland Levy-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WARNING REMAINS IN EFFECT FROM 7 PM FRIDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#       "A Winter Storm Warning remains in effect from 7 PM Friday to midnight EST Saturday night. ",
#      "|*|* SEGMENT TEXT GOES HERE *|.*|",
      "Precautionary/preparedness actions...",
#      "A Winter Storm Warning MEANS SIGNIFICANT AMOUNTS OF SNOW...SLEET...AND ICE ARE EXPECTED OR OCCURRING. STRONG WINDS ARE ALSO POSSIBLE. THIS WILL MAKE TRAVEL VERY HAZARDOUS OR IMPOSSIBLE.",
      "&&",
      "$$",
      "FLZ061-010800-",
      "/O.CON.KTBW.WS.W.0001.100102T0300Z-100103T0500Z/",
      "DeSoto-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WARNING REMAINS IN EFFECT FROM 10 PM FRIDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#       "A Winter Storm Warning remains in effect from 10 PM Friday to midnight EST Saturday night. ",
#      "|*|* SEGMENT TEXT GOES HERE *|.*|",
      "Precautionary/preparedness actions...",
#      "A Winter Storm Warning MEANS SIGNIFICANT AMOUNTS OF SNOW...SLEET...AND ICE ARE EXPECTED OR OCCURRING. STRONG WINDS ARE ALSO POSSIBLE. THIS WILL MAKE TRAVEL VERY HAZARDOUS OR IMPOSSIBLE.",
      "&&",
      "$$",
      "FLZ162-262-010800-",
      "/O.CON.KTBW.WS.W.0001.100102T1200Z-100103T0500Z/",
      "Coastal Charlotte-Inland Charlotte-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WARNING REMAINS IN EFFECT FROM 7 AM SATURDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#       "A Winter Storm Warning remains in effect from 7 AM Saturday to midnight EST Saturday night. ",
#      "|*|* SEGMENT TEXT GOES HERE *|.*|",
      "Precautionary/preparedness actions...",
#      "A Winter Storm Warning MEANS SIGNIFICANT AMOUNTS OF SNOW...SLEET...AND ICE ARE EXPECTED OR OCCURRING. STRONG WINDS ARE ALSO POSSIBLE. THIS WILL MAKE TRAVEL VERY HAZARDOUS OR IMPOSSIBLE.",
      "&&",
      "$$",
                     ],
    },
    {
    "commentary": "No changes are made to the existing hazards.",
    "name": "GHG_Complex5_6",
    "productType": "Hazard_WSW_Local",
    "deleteGrids": [],
    "checkStrings": [
      "WWUS42 KTBW 010000",
      "WSWTBW",
      "URGENT - WINTER WEATHER MESSAGE",
      "National Weather Service Tampa Bay Ruskin FL",
      "700 PM EST Thu Dec 31 2009",
      "...|*Overview headline (must edit)*|...",
      ".|*Overview (must edit)*|.",
      "FLZ142-242-010800-",
      "/O.CON.KTBW.BZ.W.0001.100102T0000Z-100103T0500Z/",
      "Coastal Citrus-Inland Citrus-",
      "700 PM EST Thu Dec 31 2009",
      "...BLIZZARD WARNING REMAINS IN EFFECT FROM 7 PM FRIDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#       "A Blizzard Warning remains in effect from 7 PM Friday to midnight EST Saturday night. ",
#      "|*|*|* SEGMENT TEXT GOES HERE *|.*|*|",
      "Precautionary/preparedness actions...",
      "A Blizzard Warning means severe winter weather conditions are expected or occurring. Falling and blowing snow with strong winds and poor visibilities are likely. This will lead to whiteout conditions...making travel extremely dangerous. Do not travel. If you must travel...have a winter survival kit with you. If you get stranded...stay with your vehicle.",
      "&&",
      "$$",
      "FLZ139-239-010800-",
      "/O.CON.KTBW.WS.W.0001.100102T0000Z-100103T0500Z/",
      "Coastal Levy-Inland Levy-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WARNING REMAINS IN EFFECT FROM 7 PM FRIDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#       "A Winter Storm Warning remains in effect from 7 PM Friday to midnight EST Saturday night. ",
#      "|*|* SEGMENT TEXT GOES HERE *|.*|",
#      "A Winter Storm Warning MEANS SIGNIFICANT AMOUNTS OF SNOW...SLEET...AND ICE ARE EXPECTED OR OCCURRING. STRONG WINDS ARE ALSO POSSIBLE. THIS WILL MAKE TRAVEL VERY HAZARDOUS OR IMPOSSIBLE.",
      "$$",
      "FLZ061-010800-",
      "/O.CON.KTBW.WS.W.0001.100102T0300Z-100103T0500Z/",
      "DeSoto-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WARNING REMAINS IN EFFECT FROM 10 PM FRIDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#       "A Winter Storm Warning remains in effect from 10 PM Friday to midnight EST Saturday night. ",
#      "|*|* SEGMENT TEXT GOES HERE *|.*|",
      "Precautionary/preparedness actions...",
#      "A Winter Storm Warning MEANS SIGNIFICANT AMOUNTS OF SNOW...SLEET...AND ICE ARE EXPECTED OR OCCURRING. STRONG WINDS ARE ALSO POSSIBLE. THIS WILL MAKE TRAVEL VERY HAZARDOUS OR IMPOSSIBLE.",
      "&&",
      "$$",
      "FLZ162-262-010800-",
      "/O.CON.KTBW.WS.W.0001.100102T1200Z-100103T0500Z/",
      "Coastal Charlotte-Inland Charlotte-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER STORM WARNING REMAINS IN EFFECT FROM 7 AM SATURDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#       "A Winter Storm Warning remains in effect from 7 AM Saturday to midnight EST Saturday night. ",
#      "|*|* SEGMENT TEXT GOES HERE *|.*|",
      "Precautionary/preparedness actions...",
#      "A Winter Storm Warning MEANS SIGNIFICANT AMOUNTS OF SNOW...SLEET...AND ICE ARE EXPECTED OR OCCURRING. STRONG WINDS ARE ALSO POSSIBLE. THIS WILL MAKE TRAVEL VERY HAZARDOUS OR IMPOSSIBLE.",
      "&&",
      "$$",
      "FLZ052-010800-",
      "/O.CON.KTBW.WW.Y.0001.100102T0300Z-100103T0500Z/",
      "Polk-",
      "700 PM EST Thu Dec 31 2009",
      "...WINTER WEATHER ADVISORY REMAINS IN EFFECT FROM 10 PM FRIDAY TO MIDNIGHT EST SATURDAY NIGHT...",
#       "A Winter Weather Advisory remains in effect from 10 PM Friday to midnight EST Saturday night. ",
#      "|*|*|* SEGMENT TEXT GOES HERE *|.*|*|",
      "Precautionary/preparedness actions...",
#      "A Winter Weather Advisory means that periods of snow...sleet...or freezing rain will cause travel difficulties. Be prepared for slippery roads and limited visibilities...and use caution while driving.",
      "&&",
      "$$",
                     ],
    }, 
    {
    "commentary": "Canceling out all hazards.",
    "name": "GHG_Complex5_7",
    "productType": None,
    "clearHazardsTable": 1,
    "checkStrings": [],
    },
    ]
       

import TestScript
def testScript(self, dataMgr):
    defaults = {
        "database": "<site>_GRID__Fcst_00000000_0000",
        "publishGrids": 0,
        "decodeVTEC": 1,
        "gridsStartTime": "20100101_0000",
        "orderStrings": 1,
        "cmdLineVars": "{('Issued By', 'issuedBy'): None}",
        "deleteGrids": [("Fcst", "Hazards", "SFC", "all", "all")],
        }
    return TestScript.generalTestScript(self, dataMgr, scripts, defaults)



