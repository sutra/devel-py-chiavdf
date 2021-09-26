--- src/python_bindings/fastvdf.cpp.orig	2021-09-26 13:21:02 UTC
+++ src/python_bindings/fastvdf.cpp
@@ -40,7 +40,7 @@ PYBIND11_MODULE(chiavdf, m) {
                                    const string& proof_blob,
                                    const uint64_t num_iterations, const uint64_t disc_size_bits, const uint64_t recursion) {
         std::string proof_blob_str(proof_blob);
-        uint8_t *proof_blob_ptr = reinterpret_cast<uint8_t *>(proof_blob_str.data());
+        uint8_t *proof_blob_ptr = reinterpret_cast<uint8_t *>(const_cast<char*>(proof_blob_str.data()));
         int proof_blob_size = proof_blob.size();
 
         return CheckProofOfTimeNWesolowski(integer(discriminant), (const uint8_t *)x_s.data(), proof_blob_ptr, proof_blob_size, num_iterations, disc_size_bits, recursion);
