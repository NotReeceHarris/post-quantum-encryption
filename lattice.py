from lattice.lm_one_time_sigs import *

# Pick your message
message: str = "QRL is awesome!"

# Step 0: Create setup parameters (with 256 bits of post-quantum security).
public_parameters = make_setup_parameters(secpar=256)

# Step 1: Key generation
secret_seed, signing_key, verification_key = keygen(pp=public_parameters, num_keys_to_gen=1)[0]

# Step 2: Sign a message
signature = sign(pp=public_parameters, otk=(secret_seed, signing_key, verification_key), msg=message)

def verify(pp: PublicParameters, otvk: OneTimeVerificationKey, msg: Message, sig: Signature) -> bool:
    sig.const_time_flag = False
    cnws = sig.get_coef_rep()
    n, w = max(i[1] for i in cnws), max(i[2] for i in cnws)
    if n > pp['vf_bd'] or w > pp['vf_wt']:
        return False

    key_ch = pp['scheme_parameters'].key_ch
    c: Challenge = make_signature_challenge(pp=pp, otvk=otvk, msg=msg)

    key_ch.const_time_flag = False
    c.const_time_flag = False
    otvk.left_key.const_time_flag = False
    otvk.right_key.const_time_flag = False

    lhs = key_ch * sig
    rhs = otvk[0] * c + otvk[1]

    return lhs == rhs

# Step 3: Verify the signature
print(verify(pp=public_parameters, otvk=verification_key, msg=message, sig=signature))