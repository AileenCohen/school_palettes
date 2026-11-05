import matplotlib.pyplot as plt
from IPython.display import HTML, display

FROGS = {
    'ramaconica': ['#3C6B78', '#538D71', '#CFA838', '#A26021', '#983E18'],
    'rispotted': ['#2A5D86', '#658C93', '#587F61', '#C4B500', '#4A4B13'],
    'ribanded': ['#0C0D0C', '#F2B705', '#F29F05', '#A65D03', '#F2F2F2'],
    'rvariabilis': ['#122F51', '#3D5689', '#8E97B5', '#E1C250', '#4D4B13'],
    'afulguritus': ['#110906', '#56601B', '#A9C248', '#B2B52A', '#8DA1A9'],
    'aminutus': ['#181011', '#512A18', '#833717', '#C4AE3D', '#C5CDC5'],
    'osotokiki': ['#29211B', '#5D4224', '#8A511B', '#BBA141', '#E1B522'],
    'oscolon': ['#432B18', '#712C0F', '#D74905', '#FFAC18', '#FBF895'],
    'ossanantonio': ['#D9D4BA', '#F2A7B5', '#F23005', '#8C0E03', '#3F402C'],
    'oslita': ['#431509', '#862D12', '#D19F36', '#EED95D', '#D0D9D0'],
    'oskoi': ['#09142A', '#B8351F', '#F88705', '#ABD0DD', '#F2F9FE'],
    'olehmanni': ['#1B110F', '#FE4705', '#F59356', '#7997A5', '#D9DFDF'],
    'oanchicayensis': ['#261717', '#5A2511', '#FA6100', '#FCC908', '#D1D3DB'],
    'ohistrionica': ['#181A0C', '#A20D05', '#F23D07', '#FB7309', '#FE8E04'],
    'opescudo': ['#46AFD2', '#CFC387', '#9EA979', '#B12F0A', '#192326'],
    'opcolon': ['#E6CD13', '#95AE26', '#E07E12', '#8B5E58', '#351D0A'],
    'oploma': ['#00262C', '#005E6C', '#00AEB0', '#21B66E', '#64B146'],
    'opsancristobal': ['#ECAA4E', '#E15511', '#48353C', '#1B5280', '#072643'],
    'opuyama': ['#9AAEB0', '#0086A1', '#214F6D', '#451A0E', '#010100'],
    'opbluejeans': ['#512118', '#D5411F', '#637C94', '#3A5169', '#181717'],
    'dtnouragues': ['#090B0A', '#263F48', '#499AC1', '#EEA715', '#FED126'],
    'dtazureus': ['#282349', '#161C4D', '#163978', '#4268B4', '#869BD7'],
    'dauratus': ['#171517', '#1B445B', '#4AA3B8', '#2AB8A2', '#96D02B'],
    'pterribilis': ['#42350C', '#6E5006', '#E19F05', '#F9C207', '#FCD94B'],
    'afemoralis': ['#171006', '#7F541B', '#FFD70A', '#E8CB99', '#D6E5CD'],
    'atrivittata': ['#15170E', '#9ACF46', '#E8F649', '#BBE5AE', '#3B95C8'],
    'amacero': ['#14374A', '#3981BE', '#64B936', '#C6E74B', '#7D2A1D'],
    'ashihuemoy': ['#151018', '#664328', '#FE9C01', '#19AC0C', '#23A7A6'],
    'eanthonyi': ['#F2DC9B', '#D95204', '#A60311', '#590202', '#0B0B0D'],
    'etricolor': ['#D9D7BA', '#4A4E8C', '#593A15', '#402B12', '#261C14'],
    'edarwinwallacei': ['#F2F2F2', '#F2D479', '#D99C52', '#403636', '#0D0A0A'],
    'bpicturata': ['#291D11', '#726241', '#9F7A6A', '#CFCDAC', '#D9D6D3'],
    'dsarayacuensis': ['#FDFFFD', '#EAD676', '#B18044', '#BE5121', '#5F3C10'],
    'haureoguttatum': ['#732937', '#565902', '#D9A404', '#D9CAB0', '#F2F2F2'],
    'hcinerascens': ['#CCB33C', '#979136', '#57724C', '#9C4E1E', '#49210D'],
    'hhobbsi': ['#EBE6D5', '#86948C', '#949C67', '#9A7726', '#4F290A'],
    'llineatus': ['#C0B956', '#C69B40', '#C75D25', '#493836', '#20110A'],
    'mlaevigata': ['#9FBF5A', '#C7D93D', '#A4A677', '#59573C', '#0D0D0D'],
    'ptomopterna': ['#C7AE91', '#648225', '#C57B2B', '#6F3812', '#240904'],
    'pvaillantii': ['#CEC4B9', '#C89353', '#979136', '#424A17', '#5E2421'],
    'rmarina': ['#D7CCA2', '#B7A05D', '#84652E', '#4B250B', '#2E1204']
}

FISH = {
    'holocentrus_adscensionis': ['#F19564', '#F2784B', '#D94B2B'],
    'zapteryx_brevirostris': ['#F2DFBB', '#BF9969', '#734C29', '#402718', '#CCB48F'],
    'gymnothorax_funebris': ['#5C732C', '#B4B611', '#43603C', '#809D5B', '#99A11F'],
    'pomacanthus_paru': ['#005281', '#000008', '#0096CB', '#D2D904', '#F28705'],
    'sparisoma_frondosum_m': ['#0477BF', '#005F8E', '#8288B2', '#5C7CAB', '#00ADDE'],
    'anisotremus_virginicus': ['#0487D9', '#BFA004', '#A6681C', '#3B3217', '#553A19'],
    'epinephelus_marginatus': ['#7D8556', '#784849', '#553748', '#C1892D', '#95C0A1'],
    'acanthisthius_brasilianus': ['#527E87', '#B88244', '#B8B69E', '#B48F2C', '#A37903'],
    'labrisomus_cricota': ['#764743', '#2F3033', '#BC846C', '#F2785C', '#8C423B'],
    'serranus_baldwini': ['#048ABF', '#474F3E', '#F2B705', '#A64F03', '#BF3030'],
    'elacatinus_figaro': ['#1C1C1B', '#FFEB08', '#F2CB05', '#F2B705', '#AEB021'],
    'hamulon_plumieri': ['#63BBF2', '#4997F0', '#5E5B04', '#A66D03', '#8C5D23'],
    'hippocampus_reidi': ['#F2CB05', '#F2B705', '#D98E04', '#D57326', '#8C310F'],
    'pseudupeneus_maculatus': ['#7C4333', '#D59F00', '#A6662E', '#F22222', '#36211A'],
    'myrichthys_ocellatus': ['#C3BF9D', '#FFC700', '#FFE624', '#848176', '#535157'],
    'acanthostracion_polygonius_y': ['#491212', '#F27127', '#F24C27', '#BF281B', '#CE471C'],
    'halichoeres_brasiliensis': ['#056CF2', '#0583F2', '#05AFF2', '#05C7F2', '#05DBF2'],
    'thalassoma_noronhanum': ['#84D4E9', '#04C4D9', '#04D9C4', '#A77848', '#AC5E91'],
    'hypsoblennius_invemar': ['#30618C', '#21355D', '#229BAE', '#E3E2C3', '#D65638'],
    'harengula_jaguana': ['#7995C1', '#7B8C95', '#A7B8A6', '#F0EBE7', '#FAC2AF'],
    'opisthonema_oglinum': ['#366698', '#52838C', '#767F8F', '#72ABB1', '#E3ECE9'],
    'lile_piquitinga': ['#857C3C', '#7C7056', '#595741', '#373C38', '#CAD9D6'],
    'sardinella_brasiliensis': ['#798962', '#A9BDB5', '#8DA5BE', '#A1C7DC', '#D3EEFE'],
    'lycengraulis_grossidens': ['#C29315', '#B4945C', '#D3D1CF', '#D7EDF1', '#EDF9F9'],
    'anchoviella_lepidentostole': ['#8A7036', '#937366', '#CE9B89', '#A7988D', '#E7E9E4'],
    'cetengraulis_edentulus': ['#806607', '#807A50', '#5C6560', '#9BA59D', '#A6AEA6'],
    'atherinella_brasiliensis': ['#677381', '#917249', '#B1A5A0', '#BFB4AC', '#E7E2DA'],
    'mugil_liza': ['#4E4139', '#888862', '#B5AFB1', '#D6D5DB', '#E4EDF4'],
    'pareiorhaphis_garbei': ['#49351C', '#624D1E', '#A13601', '#C67E22', '#BA8D55'],
    'paralabrax_clathratus': ['#43431D', '#7D804B', '#A9A56D', '#D3C793', '#E6EEE0'],
    'semicossyphus_pulcher': ['#242427', '#794B3E', '#9D6359', '#CDAD9D', '#E8DDD7'],
    'phractocephalus_hemioliopterus': ['#C11800', '#ED5903', '#E8B332', '#80695C', '#C5C7A7'],
    'micropterus_punctulatus': ['#727250', '#655323', '#2A2712', '#B3AC66', '#434727'],
    'neogobius_melanostomus': ['#64CCFC', '#EDE27B', '#BB904E', '#825841', '#1A0202'],
    'thunnus_obesus': ['#669ABF', '#D4D05B', '#FDF6E2', '#747798', '#534D56'],
    'barbus_barbus': ['#6B472C', '#8D4F20', '#CA925B', '#CFC99F', '#89AAC6'],
    'alosa_fallax': ['#7992A6', '#C0D1CE', '#BCB584', '#70684D', '#383733'],
    'sander_lucioperca': ['#F1ECEB', '#B3B0AF', '#93745C', '#522F1D', '#3E2528'],
    'esox_lucius': ['#E1E2DD', '#C6C7B6', '#BBA88A', '#935933', '#5C2C18'],
    'petromyzon_marinus': ['#514337', '#7B533E', '#9C7148', '#AC955F', '#ADA185'],
    'pleuronectes_platessa': ['#D5531F', '#B23B09', '#794422', '#A56029', '#D29C63'],
    'gadus_morhua': ['#5D784C', '#ADDAB3', '#778E3F', '#B1F0EE', '#6E927D'],
    'ctenochaetus_strigosus': ['#FEFB51', '#EFA904', '#8F6D67', '#644C71', '#20A6F8']
}

LTC = {
    'paloma': ['#83AF9B', '#C8C8A9', '#F8DA8A', '#F7BF95', '#FE8CA1'],
    'maya': ['#3D5A80', '#98C1D9', '#E0FBFC', '#EE6C4D', '#293241'],
    'dora': ['#52777A', '#542437', '#C02942', '#D95B43', '#ECD078'],
    'ploen': ['#3F5671', '#83A1C3', '#CEB5C8', '#FAC898', '#B17776'],
    'olga': ['#C9E3C2', '#8BC8CB', '#ECCD80', '#F5AB70', '#9C87A1'],
    'mterese': ['#F7DDAA', '#FAC3AD', '#F897A1', '#9298BA', '#9CBEED'],
    'gaby': ['#FCEAAB', '#F1A890', '#A8C4CC', '#82A0C2', '#85496F'],
    'franscoise': ['#5980B1', '#B96A8D', '#A55062', '#E05256', '#E9A986'],
    'fernande': ['#FF7676', '#F9D662', '#7CAB7D', '#75B7D1'],
    'sylvie': ['#E8B961', '#E88170', '#C6BDE8', '#5DB7C4', '#FD95BC'],
    'expevo': ['#FC4E07', '#E7B800', '#00AFBB', '#8B4769', '#1D457F', '#808080'],
    'minou': ['#00798C', '#D1495B', '#EDAE49', '#66A182', '#2E4057', '#8D96A3'],
    'kiss': ['#FF7C7E', '#FEC300', '#9E3F71', '#31BCBA', '#E20035'],
    'hat': ['#EFB306', '#EB990C', '#E8351E', '#CD023D', '#852F88', '#4E54AC', '#0F8096', '#7DB954', '#17A769', '#000000'],
    'reading': ['#EFBC68', '#919F89', '#EDBDAE', '#57717C', '#5F97A4', '#CAEAC8', '#95A1AE', '#C8CFD6'],
    'alger': ['#000000', '#1A5B5B', '#ACC8BE', '#F4AB5C', '#D1422F'],
    'trio1': ['#0E7175', '#FD7901', '#C35BCA'],
    'trio2': ['#89973D', '#E8B92F', '#A45E41'],
    'trio3': ['#E69F00', '#56B4E9', '#009E73'],
    'trio4': ['#94475E', '#364C54', '#E5A11F'],
    'heatmap0': ['#001219', '#005F73', '#0A9396', '#94D2BD', '#E9D8A6', '#EE9B00', '#CA6702', '#AE2012', '#9B2226'],
    'pantone23': ['#7A92A5', '#1F2C43', '#FFB000', '#842C48', '#46483D'],
    'remains': ['#69326E', '#EEEDC0', '#FF6D1F', '#EED455'],
    'midnight': ['#16232A', '#FF5B04', '#075056', '#E4EEF0'],
    'lincoln': ['#EEE9DF', '#C9C1B1', '#2C3B4D', '#FFB162', '#A35139', '#1B2632'],
    'luminaries': ['#FF5B04', '#075056', '#233038', '#FDF6E3', '#F4D47C', '#D3DBDD'],
    'seafarer': ['#013D5A', '#FCF3E3', '#BDD3CE', '#708C69', '#E4A25B'],
    'shuggie': ['#5B5F8D', '#9BB29E', '#DA6B51', '#F1DCBA', '#484149'],
    'heatmap1': ['#4D7799', '#7FA4C4', '#C5C8D4', '#D48E95', '#B5515B'],
    'heatmap2': ['#CA0020', '#F4A582', '#F7F7F7', '#92C5DE', '#0571B0'],
    'heatmap3': ['#D7191C', '#FDAE61', '#FFFFBF', '#ABD9E9', '#2C7BB6'],
    'casa_natal': ['#245E55', '#ED773C', '#808BC5', '#C63F3E', '#EAC119', '#EAA7C7', '#9ED6DF', '#1D1D1B', '#EAE4DA']
}

NATURE = {
    'earthy_forest_hues': ['#DAD7CD', '#A3B18A', '#588157', '#3A5A40', '#344E41'],
    'natures_harmony': ['#004733', '#2B6A4D', '#568D66', '#A5C1AE', '#F3F4F6'],
    'mossy_creek': ['#223A33', '#3F6B5B', '#7AA88F', '#B7C9B9', '#F2EFE6'],
    'sunlit_meadow': ['#4F7D3A', '#A8C66C', '#F1D88A', '#E9B08B', '#FFF6E7'],
    'canyon_clay': ['#7A4B2A', '#B06A3B', '#D6A16A', '#6B7A4E', '#F3EADF'],
    'ocean_kelp': ['#0F2F2E', '#1F5B57', '#4A7F6A', '#B9CBB7', '#F7F3EA'],
    'leafy_green_garden': ['#132A13', '#31572C', '#4F772D', '#90A955', '#ECF39E'],
    'earthy_tones': ['#EDAFB8', '#F7E1D7', '#DEDBD2', '#B0C4B1', '#4A5759'],
    'vibrant_nature': ['#DA2C38', '#226F54', '#87C38F', '#F4F0BB', '#43291F'],
    'pine_and_bark': ['#283618', '#606C38', '#FEFAE0', '#DDA15E', '#BC6C25'],
    'misty_mountain': ['#2F3E46', '#354F52', '#52796F', '#84A98C', '#CAD2C5'],
    'deep_sea_trench': ['#03045E', '#023E8A', '#0077B6', '#0096C7', '#48CAE4'],
    'desert_sandstone': ['#C68B59', '#D8B384', '#F4EBE1', '#583D72', '#FF7B54'],
    'autumn_canopy': ['#331800', '#70290A', '#C25923', '#E69A33', '#F5D676'],
    'spring_blossom': ['#FFB5A7', '#FCD5CE', '#F8EDEB', '#F9DCC4', '#FEC89A'],
    'tropical_rainforest': ['#0A3A18', '#1B4332', '#2D6A4F', '#40916C', '#52B788'],
    'arctic_glacier': ['#E0FBFC', '#C2DFE3', '#9DB4CD', '#5C6B73', '#253237'],
    'savanna_sunset': ['#2B2D42', '#8D99AE', '#EDF2F4', '#EF233C', '#D90429'],
    'wildflower_meadow': ['#785964', '#6D6875', '#B5838D', '#E5989B', '#FFB703'],
    'river_stone': ['#3A3A3A', '#5C6B73', '#9DB4CD', '#C2DFE3', '#E0FBFC'],
    'bamboo_grove': ['#386641', '#6A994E', '#A7C957', '#F2E8CF', '#BC4749'],
    'volcanic_ash': ['#1A1A1A', '#4D4D4D', '#808080', '#B3B3B3', '#E6E6E6'],
    'coral_reef': ['#FF6F59', '#FF9A8B', '#FF6A88', '#FF99AC', '#43C6AC'],
    'tundra_moss': ['#4A4E36', '#606C38', '#7F8C8D', '#BDC3C7', '#ECF0F1'],
    'canyon_sunset': ['#541388', '#F1E9DA', '#FFD400', '#D90368', '#2E294E'],
    'herbal_tea': ['#556B2F', '#8FBC8F', '#BDB76B', '#F5DEB3', '#FFF8DC'],
    'eucalyptus_mist': ['#6B8E23', '#808000', '#B0C4DE', '#E6EFAF', '#F4F4F4'],
    'terracotta_pot': ['#E2725B', '#D96B43', '#C85A32', '#9E472A', '#70331D'],
    'sun_baked_soil': ['#3D2817', '#593C22', '#8C5E35', '#BF895A', '#E3BC9A'],
    'glacial_lake': ['#005F73', '#0A9396', '#94D2BD', '#E9D8A6', '#EE9B00'],
    'cedar_forest': ['#1A2E26', '#2D4A3E', '#4A7061', '#759B8C', '#B5C7BF'],
    'midnight_jungle': ['#0B131F', '#1C2D37', '#2B454E', '#3E606F', '#8CBEB2'],
    'golden_savannah': ['#C19A6B', '#D4B28C', '#E6CAAD', '#F7E2CE', '#FFF5EB'],
    'slate_and_lichen': ['#2C3539', '#437C17', '#728C00', '#B5B8B1', '#E5E4E2'],
    'coastal_dune': ['#F3E5AB', '#D4C38E', '#B39D72', '#8C7355', '#5E4A35'],
    'deep_fen': ['#1E2F23', '#334734', '#526E52', '#7A9A7A', '#B2CFC2'],
    'amber_woods': ['#4B382A', '#725C44', '#9E8164', '#C8B199', '#EFE3D4'],
    'boreal_night': ['#0F172A', '#1E293B', '#334155', '#475569', '#64748B'],
    'honey_and_clover': ['#FEFAE0', '#D4A373', '#CCD5AE', '#E9EDC9', '#FAEDCD'],
    'stormy_sky': ['#2B3A42', '#3F525B', '#586E75', '#889A9C', '#C5D1D1'],
    'autumn_harvest': ['#8D230F', '#A8411D', '#C66B27', '#E5953F', '#F3C68F'],
    'spring_sprout': ['#E9F5DB', '#CFE1B9', '#B5C99A', '#87A330', '#556B2F'],
    'muted_peat': ['#3B3024', '#5C4E3E', '#85735D', '#B2A28C', '#E3DCD0'],
    'subtropical_teal': ['#003B46', '#07575B', '#66A5AD', '#C4DFE6', '#EDEDED'],
    'redwood_bark': ['#4D2C1D', '#663C27', '#804D33', '#995E40', '#B36F4D'],
    'sea_salt': ['#F8F9FA', '#E9ECEF', '#DEE2E6', '#CED4DA', '#ADB5BD'],
    'chaparral_brush': ['#5A6B46', '#8A9A68', '#B5C299', '#D8E2C4', '#F0F4E8'],
    'freshwater_stream': ['#D8F3DC', '#B7E4C7', '#95D5B2', '#74C69D', '#52B788'],
    'smoky_quartz': ['#3E3836', '#5C5350', '#7A706D', '#A39B98', '#D6D0CD'],
    'evergreen_ridge': ['#122620', '#1B3B32', '#2D5A4C', '#468572', '#79B4A9']
}

ALL_PALETTES = {**FROGS, **FISH, **LTC, **NATURE}

class SubLibrary:
    def __init__(self, name, palettes_dict):
        self._name = name
        self._palettes = palettes_dict
        for k, v in palettes_dict.items():
            setattr(self, k, v)
            
    def __repr__(self):
        return f"<School Sub-Library: {self._name} ({len(self._palettes)} palettes)>"

class School:
    def __init__(self):
        self.frogs = SubLibrary('frogs', FROGS)
        self.fish = SubLibrary('fish', FISH)
        self.ltc = SubLibrary('ltc', LTC)
        self.nature = SubLibrary('nature', NATURE)
        
        for k, v in ALL_PALETTES.items():
            setattr(self, k, v)

    def show_table(self, sub_lib_name=None):
        target_dict = ALL_PALETTES
        title = "All Palettes"
        
        if sub_lib_name:
            sub_lib_name = sub_lib_name.lower()
            if sub_lib_name == 'frogs':
                target_dict = FROGS
            elif sub_lib_name == 'fish':
                target_dict = FISH
            elif sub_lib_name == 'ltc':
                target_dict = LTC
            elif sub_lib_name == 'nature':
                target_dict = NATURE
            else:
                print(f"Unknown sub-library: '{sub_lib_name}'. Showing all instead.")
            title = f"Sub-Library: '{sub_lib_name}'"

        html_output = f"<h3>🏫 {title}</h3>"
        html_output += "<table style='border-collapse: collapse; width: 100%; font-family: sans-serif;'>"
        html_output += "<tr style='background-color: #f2f2f2;'><th style='padding: 10px; text-align: left; border-bottom: 2px solid #ddd;'>Palette Name</th>"
        html_output += "<th style='padding: 10px; text-align: left; border-bottom: 2px solid #ddd;'>Colors Preview</th></tr>"
        
        for pal_name, colors in target_dict.items():
            color_stops = []
            num_colors = len(colors)
            for idx, color in enumerate(colors):
                start = (idx / num_colors) * 100
                end = ((idx + 1) / num_colors) * 100
                color_stops.append(f"{color} {start}% {end}%")
            
            gradient_str = ", ".join(color_stops)
            preview_style = f"background: linear-gradient(to right, {gradient_str}); width: 300px; height: 30px; border-radius: 4px; border: 1px solid #ccc;"
            
            html_output += f"<tr><td style='padding: 10px; font-weight: bold; border-bottom: 1px solid #eee;'>{pal_name}</td>"
            html_output += f"<td style='padding: 10px; border-bottom: 1px solid #eee;'><div style='{preview_style}'></div></td></tr>"
            
        html_output += "</table>"
        display(HTML(html_output))
