# Coffer

Coffer is a small application that encrypts and stores documents in 
Amazon S3. Coffer uses KMS to generate data encryption keys that are used
to encrypt your data. The data encryption keys are themselves encrypted
with a master key so that they can be stored safely and retrieved when
needed.
