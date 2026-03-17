import argparse
from src.witness.cert.serializer import load_certificate
from src.witness.cert.certificate import RigidityCertificate

def identity(x):
    return x

TRANSFORMS = {"identity": identity}

def main():
    parser = argparse.ArgumentParser(description="Verify a terminal rigidity certificate")
    parser.add_argument("certificate")
    args = parser.parse_args()

    cert = load_certificate(args.certificate, TRANSFORMS)
    ok = cert.validate()

    if ok:
        print("Certificate VALID")
    else:
        print("Certificate INVALID")

if __name__ == "__main__":
    main()
