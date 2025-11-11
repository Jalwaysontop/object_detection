import yaml
with open("config/pixel_focal_length.yaml","r+") as f:
    data=yaml.load(f,Loader=yaml.SafeLoader)
    p_avg=data['calibration']["P_avg"]
    width=data['calibration']['box_object_width_cm']
    distance=data['calibration']['known_distance_cm']
    focal_length=p_avg*distance/width
    new_confi={
        "focal_length_pixel":focal_length
    }
    yaml.dump(new_confi,f)
