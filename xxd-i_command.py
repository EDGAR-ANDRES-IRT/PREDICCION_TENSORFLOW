#Realiza la misma función que el comando xxd -i en linux

with open("predictor.tflite", "rb") as f:
    data = f.read()

with open("model_data.cc", "w") as f:
    f.write("const unsigned char model[] = {\n")
    for i, byte in enumerate(data):
        f.write(f"0x{byte:02x}, ")
        if (i + 1) % 12 == 0:
            f.write("\n")
    f.write("\n};\n")
    f.write(f"const int model_len = {len(data)};\n")