import hid

def change_device(hidapi_device, device_type='keyboard'):
    hidapi_device.nonblocking = 1

    print(f"Device: {hidapi_device} $$$ Device type: {device_type}")
    if device_type == 'mouse':
        try:
            switch_mouse_from_2_to_1 = b"\x11\x02\x0A\x1B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            hidapi_device.write(switch_mouse_from_2_to_1)
        except Exception as e:
            try:
                switch_mouse_from_1_to_2 = b"\x11\x02\x09\x1C\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                hidapi_device.write(switch_mouse_from_1_to_2)
            except Exception as e:
                print("Can't switch mouse")

    # if device_type == 'mouse':
    #     if device_switcher == '1_to_2':
    #         switch_mouse_from_1_to_2 = b"\x11\x01\x0A\x1B\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    #         hidapi_device.write(switch_mouse_from_1_to_2)    
    #     if device_switcher == '2_to_1':
    #         switch_mouse_from_2_to_1 = b"\x11\x01\x09\x1C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"      
    #         hidapi_device.write(switch_mouse_from_2_to_1)
        
    # switch_keyboard_from_1_to_2 = b"\x11\x02\x09\x1C\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    # hidapi_device.write(switch_keyboard_from_1_to_2)
    
    
    # switch_mouse_from_1_to_2 = b"\x11\x01\x0A\x1B\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    # hidapi_device.write(switch_mouse_from_1_to_2)    
    # switch_mouse_from_2_to_1 = b"\x11\x01\x09\x1C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"      
    # hidapi_device.write(switch_mouse_from_2_to_1)


def main():
    select_devices = {
        'vendor_id': 0x46d,
        'MX Master 3S': 'mouse', 
        # 'MX KEYS S': 'keyboard' 
    } 
    device_list = hid.enumerate(select_devices.get('vendor_id'))
    for device in device_list:
        if device.get('product_string') in select_devices:
            print(f"\n\n==== Found device: {device.get('product_string')} - {device}\n")
            try:
                h = hid.Device(device.get('vendor_id'), device.get('product_id'))
                print(vars(h))
                change_device(h, select_devices.get(device.get('product_string')))
            except Exception as e:
                print(f"Error: {e}")
                continue
    