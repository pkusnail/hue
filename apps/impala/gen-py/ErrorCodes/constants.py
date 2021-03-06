#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *

TErrorMessage = [
  "",
  "$0",
  "$0",
  "$0",
  "$0",
  "$0",
  "$0",
  "$0",
  "$0",
  "Parquet files should not be split into multiple hdfs-blocks. file=$0",
  "Column metadata states there are $0 values, but read $1 values from column $2. file=$3",
  "(unused)",
  "ParquetScanner: reached EOF while deserializing data page header. file=$0",
  "Metadata states that in group $0($1) there are $2 rows, but $3 rows were read.",
  "(unused)",
  "File '$0' column '$1' does not have the decimal precision set.",
  "File '$0' column '$1' has a precision that does not match the table metadata  precision. File metadata precision: $2, table metadata precision: $3.",
  "File '$0' column '$1' does not have converted type set to DECIMAL",
  "File '$0' column '$1' contains decimal data but the table metadata has type $2",
  "Problem parsing file $0 at $1$2",
  "Decompressor: block size is too big.  Data is likely corrupt. Size: $0",
  "Decompressor: invalid compressed length.  Data is likely corrupt.",
  "Snappy: GetUncompressedLength failed",
  "SnappyBlock: RawUncompress failed",
  "Snappy: Decompressed size is not correct.",
  "Unknown disk id.  This will negatively affect performance. Check your hdfs settings to enable block location metadata.",
  "Reserved resource size ($0) is larger than query mem limit ($1), and will be restricted to $1. Configure the reservation size by setting RM_INITIAL_MEM.",
  "Cannot perform join at hash join node with id $0. The input data was partitioned the maximum number of $1 times. This could mean there is significant skew in the data or the memory limit is set too low.",
  "Cannot perform aggregation at hash aggregation node with id $0. The input data was partitioned the maximum number of $1 times. This could mean there is significant skew in the data or the memory limit is set too low.",
  "Builtin '$0' with symbol '$1' does not exist. Verify that all your impalads are the same version.",
  "RPC Error: $0",
  "RPC timed out",
  "Failed to verify function $0 from LLVM module $1, see log for more details.",
  "File $0 corrupt. RLE level data bytes = $1",
  "Column '$0' has conflicting Avro decimal types. Table schema $1: $2, file schema $1: $3",
  "Column '$0' has conflicting Avro decimal types. Declared $1: $2, $1 in table's Avro schema: $3",
  "Unresolvable types for column '$0': table type: $1, file type: $2",
  "Unresolvable types for column '$0': declared column type: $1, table's Avro schema type: $2",
  "Field $0 is missing from file and default values of type $1 are not yet supported.",
  "Inconsistent table metadata. Mismatch between column definition and Avro schema: cannot read field $0 because there are only $1 fields.",
  "Field $0 is missing from file and does not have a default value.",
  "Field $0 is nullable in the file schema but not the table schema.",
  "Inconsistent table metadata. Field $0 is not a record in the Avro schema.",
  "Could not read definition level, even though metadata states there are $0 values remaining in data page. file=$1",
  "Mismatched number of values in column index $0 ($1 vs. $2). file=$3",
  "Failed to decode dictionary-encoded value. file=$0",
  "SSL private-key password command ('$0') failed with error: $1",
  "The SSL certificate path is blank",
  "The SSL private key path is blank",
  "The SSL certificate file does not exist at path $0",
  "The SSL private key file does not exist at path $0",
  "SSL socket creation failed: $0",
  "Memory allocation of $0 bytes failed",
  "Could not read repetition level, even though metadata states there are $0 values remaining in data page. file=$1",
  "File '$0' has an incompatible Parquet schema for column '$1'. Column type: $2, Parquet schema:\n$3",
  "Failed to allocate buffer for collection '$0'.",
  "Temporary device for directory $0 is blacklisted from a previous error and cannot be used.",
  "Temporary file $0 is blacklisted from a previous error and cannot be expanded.",
  "RPC client failed to connect: $0",
  "Metadata for file '$0' appears stale. Try running \"refresh $1\" to reload the file metadata.",
  "File '$0' has an invalid version number: $1\nThis could be due to stale metadata. Try running \"refresh $2\".",
  "Tried to read $0 bytes but could only read $1 bytes. This may indicate data file corruption. (file $2, byte offset: $3)",
  "Invalid read of $0 bytes. This may indicate data file corruption. (file $1, byte offset: $2)",
  "File '$0' has an invalid version header: $1\nMake sure the file is an Avro data file.",
  "Enabling server-to-server SSL connections in conjunction with Kerberos authentication is not supported at the same time. Disable server-to-server SSL by unsetting --ssl_client_ca_certificate.",
]
